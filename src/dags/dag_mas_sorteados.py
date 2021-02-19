from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_mas_sorteados as facade

dag = DAG('5__numeros_mas_sorteados',
          default_args={'owner': 'Ned'},
          description='mostrar os numeros mas sorteados',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )


op1 = PythonOperator(task_id="__MEGA__mas_sorteados",
                     provide_context=True,
                     python_callable=facade.statisticas,
                     dag=dag)

op1
