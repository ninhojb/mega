from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from python import mega_mostrar_todos_jogos as facade

dag = DAG('3__mostrar_numeros__todos',
          default_args={'owner': 'NEd'},
          description='mostrar os todos numeros gerados',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False
          )


op1 = PythonOperator(task_id="__MEGA__mostrar_numeros",
                     provide_context=True,
                     python_callable=facade.mostrar_jogos_gerados,
                     dag=dag)

op1
