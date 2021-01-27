from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from src.python.root import mega as facade

dag = DAG('__gerador_numeros',
          default_args={'owner': 'CM', 'catchup': False},
          description='gerador de numeros',
          schedule_interval=None,  # '0 10 * * *',
          start_date=(datetime.combine(datetime.today() - timedelta(1), datetime.min.time())),
          max_active_runs=1,
          catchup=False,
          )

op_names = []

_op_prefix = 'gerar'

op_names.append(f'{_op_prefix}numeros')
op1 = PythonOperator(task_id=op_names[-1],
                     provide_context=False,
                     python_callable=facade.gerar(),
                     dag=dag)

dag >> op1
