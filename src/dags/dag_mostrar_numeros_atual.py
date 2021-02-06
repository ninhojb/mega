from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_mostrar_jogos_atuais as facade

dag = DAG('2__mostrar_numeros__atuais',
          default_args={'owner': 'Ned'},
          description='Mostra numeros do dia',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )

op1 = PythonOperator(task_id="__Mega__mostrar_jogos_atuais",
                     provide_context=True,
                     python_callable=facade.mostrar_jogos_atuais,
                     dag=dag)

op1
