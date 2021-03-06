from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_gerar_numeros as facade

dag = DAG('1__gerador_numeros__mega',
          default_args={'owner': 'Ned'},
          description='gerador de numeros',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )

op1 = PythonOperator(task_id="__Mega__gerar_num",
                     provide_context=True,
                     python_callable=facade.mega_gerar,
                     dag=dag)

op1
