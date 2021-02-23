from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_num_mais_jogados as facade

dag = DAG('5__pegar_num_mas_jogados__mega',
          default_args={'owner': 'Ned'},
          description='pegar mais jogados da mega',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )

op1 = PythonOperator(task_id="__Mega__mais_jogados",
                     provide_context=True,
                     python_callable=facade.num_mais_jogados,
                     dag=dag)

op1
