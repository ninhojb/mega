from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_resultado as facade

dag = DAG('4__pegar_resultado__mega',
          default_args={'owner': 'Ned'},
          description='pegar resultado da mega',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )

op1 = PythonOperator(task_id="__Mega__resultado",
                     provide_context=True,
                     python_callable=facade.resultado_mega,
                     dag=dag)

op1
