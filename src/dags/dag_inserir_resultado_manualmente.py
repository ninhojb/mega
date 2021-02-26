from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_inserir_resultado_manualmente as facade

dag = DAG('7__inserir_resultado__manu',
          default_args={'owner': 'Ned'},
          description='inserir_resultado__manu',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )

op1 = PythonOperator(task_id="__Mega__resultado",
                     provide_context=True,
                     python_callable=facade.inserir_resultado_manualmente,
                     dag=dag)

op1
