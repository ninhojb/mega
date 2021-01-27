from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega as facade

dag = DAG('__gerador_numeros',
          default_args={'owner': 'teste'},
          description='gerador de numeros',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          # catchup=False
          )

op1 = PythonOperator(task_id="Teste",
                     provide_context=True,
                     python_callable=facade.gerar,
                     dag=dag)

op1
