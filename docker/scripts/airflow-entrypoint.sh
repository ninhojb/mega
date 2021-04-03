#!/usr/bin/env bash
airflow db upgrade
airflow webserver
sudo docker exec -it docker_webserver_1 bash
airflow users create -r Admin -u admin -e ninhojb@gmail.com -f admin -l user -p Mastermind@10
airflow users create -r Admin -u ninhojb -e ninhojb@gmail.com -f admin -l user -p Mastermind@10