#!/usr/bin/env bash
airflow db upgrade
airflow webserver
airflow users create -r Admin -u admin -e ninhojb@gmail.com -f admin -l user -p Mastermind@10
airflow users create -r Admin -u ninhojb -e ninhojb@gmail.com -f admin -l user -p Mastermind@10