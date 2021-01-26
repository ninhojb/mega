import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.hooks.http_hook import HttpHook
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator


def get_git_credentials_task(dag, params, git_conn):
    bash_command = 'echo "machine github.com login {{ params.login }} password {{ params.pwd }}" > ~/.netrc'

    temp_task = BashOperator(
        task_id='set_git_credentials',
        bash_command=bash_command,
        params={'login': git_conn.login,
                'pwd': git_conn.password},
        dag=dag)

    return temp_task


def get_git_clone(dag, params, nm_projeto, git_conn):
    bash_command = 'if [[ ! -e ~/workspace/{{params.project_name}}/README.md ]]; then git clone {{params.git_repo}} ~/workspace/{{params.project_name}}; else echo "Projeto [{{params.project_name}}] ja clonado"; fi'

    temp_task = BashOperator(
        task_id='git_clone',
        bash_command=bash_command,
        params={'project_name': nm_projeto,
                'git_repo': git_conn.host},
        dag=dag)

    return temp_task


def get_git_branch(dag, params):
    bash_command = "cd {{ params.source_path }};git fetch; git branch --no-track {{params.git_branch}} refs/remotes/origin/{{params.git_branch}};git branch --set-upstream-to=origin/{{params.git_branch}} {{params.git_branch}};git checkout {{params.git_branch}}"

    temp_task = BashOperator(
        task_id='git_checkout_branch',
        bash_command=bash_command,
        params=params,
        dag=dag)

    return temp_task


def get_git_credentials_cleanup_task(dag, params):
    temp_task = BashOperator(
        task_id='cleanup_git_credentials',
        bash_command='echo "" > ~/.netrc',
        dag=dag)

    return temp_task


def get_git_pull_task(dag, params):
    bash_command = "cd {{ params.source_path }}; git pull"

    temp_task = BashOperator(
        task_id='git_pull',
        bash_command=bash_command,
        params=params,
        dag=dag)

    return temp_task


def get_set_permission_task(dag, params):
    bash_command = "chmod +x {{ params.source_path }}/{{ params.deploy_script_file }}"

    temp_task = BashOperator(
        task_id='set_permission',
        bash_command=bash_command,
        params=params,
        dag=dag)

    return temp_task


def get_execute_deploy(dag, params):
    bash_command = "cd {{ params.source_path }}; ./{{ params.deploy_script_file }}"

    temp_task = BashOperator(
        task_id='execute_deploy',
        bash_command=bash_command,
        params=params,
        dag=dag)

    return temp_task


nm_projeto = os.getenv('ALDATA__ENV__PROJECT_NAME') or ''
conn_name = os.getenv('ALDATA__ENV__DAG_GIT')
deploy_script = os.getenv('ALDATA__ENV__DEPLOY_SCRIPT') or 'src/ci/deploy_dags.sh'
params = {
    'git_connection_id': conn_name,
    'source_path': '~/workspace/%s' % nm_projeto,
    'deploy_script_file': deploy_script,
    'git_branch': Variable.get(f'{nm_projeto}__deploy_git_branch') or 'master'
}

# print('\n\n{{%s}}\n\n' % params)

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                  datetime.min.time())

dag = DAG('__ed__deploy_from_git',
          default_args={'owner': 'Engenharia', 'catchup': False},
          description='Fluxo de deploy das DAGs do projeto [%s]' % nm_projeto,
          schedule_interval=None,  # '0 10 * * *',
          start_date=seven_days_ago,
          max_active_runs=1,
          catchup=False,
          )

git_conn = HttpHook().get_connection(params['git_connection_id'])

task_git_credentials = get_git_credentials_task(dag, params, git_conn)
task_git_clone = get_git_clone(dag, params, nm_projeto, git_conn)
task_git_branch = get_git_branch(dag, params)
task_git_pull = get_git_pull_task(dag, params)
task_git_credentials_cleanup = get_git_credentials_cleanup_task(dag, params)
task_set_permissions = get_set_permission_task(dag, params)
task_execute_deploy = get_execute_deploy(dag, params)

task_git_credentials >> task_git_clone
task_git_clone >> task_git_branch
task_git_branch >> task_git_pull
task_git_pull >> task_git_credentials_cleanup
task_git_credentials_cleanup >> task_set_permissions
task_set_permissions >> task_execute_deploy
