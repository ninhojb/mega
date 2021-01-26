#!/usr/bin/env bash

: "${FERNET_KEY:=${AIRFLOW__CORE__FERNET_KEY}}"

HR="***********************************************************************************"
PRE="-----"

echo
echo "${HR}"
echo "* Projeto: ${ALDATA__ENV__PROJECT_NAME}"
echo "* ** Realiza configuracoes basicas do airflow"
echo "* ** Esse script roda apenas uma vez e eh deletado apos execucao pelo /entrypoint.sh"
echo "${HR}"
echo ""

echo "${PRE} USERS"
airflow create_user -r Admin -u admin -e suporte@vozcobranca.com.br -f admin -l user -p Sucesso@2019
airflow create_user -r User -u user -e null@none.com -f user -l user -p Prudencia@2019

echo "${PRE} VARIABLES"
echo "${PRE}${PRE} Banco de Dados - OLTP"
airflow variables --set oltp_conn_host 192.168.254.203
airflow variables --set oltp_conn_database "C:\Program Files (x86)\Virtua\Cobranca\Dados_Interbase\COB_DB_COBRANCA.FDB"
airflow variables --set oltp_conn_user SYSDBA
airflow variables --set oltp_conn_passwd virtuakey
airflow variables --set oltp_conn_port 3050

echo "${PRE}${PRE} Banco de Dados - Postgres - RAW"
airflow variables --set raw_conn_host dev_postgres_1
airflow variables --set raw_conn_database "voz_dw"
airflow variables --set raw_conn_user aldata
airflow variables --set raw_conn_passwd Foco@2020
airflow variables --set raw_conn_port 5432

echo "${PRE}${PRE} Banco de Dados - Postgres - DW"
airflow variables --set dw_conn_host dev_postgres_1
airflow variables --set dw_conn_database "voz_dw"
airflow variables --set dw_conn_user aldata
airflow variables --set dw_conn_passwd Foco@2020
airflow variables --set dw_conn_port 5432

echo "${PRE}${PRE} Banco de Dados - Postgres - META"
airflow variables --set meta_conn_host dev_postgres_1
airflow variables --set meta_conn_database "voz_dw"
airflow variables --set meta_conn_user aldata
airflow variables --set meta_conn_passwd Foco@2020
airflow variables --set meta_conn_port 5432

echo "${PRE}${PRE} Mailchimp"
airflow variables --set mailchimp_api_key adbbb347a63dd7dbda5beb188f972911-us4

echo "${PRE}${PRE} BestVoice"
airflow variables --set bestvoice_user aldata
airflow variables --set bestvoice_passwd voz@321

echo "${PRE}${PRE} URL API Portal Voz"
airflow variables --set portal_voz_api_url https://api.grupovoz.com.br/portal/OTk5OTA1OTgzMDQ2MDAwMTkx

echo "${PRE}${PRE} Fastway"
airflow variables --set fastway_path_arquivo /data/airflow/discador/

echo "${PRE}${PRE} Formato JSON"

echo "${PRE}${PRE}${PRE} Python Examples"
airflow variables -i /conf__simple_python_example.json

echo "${PRE}${PRE}${PRE} Retorno Campanhas"
airflow variables -i /conf__campanha_retorno_email_mailchimp.json

echo "${PRE}${PRE}${PRE} Extracao"
echo "${PRE}${PRE}${PRE}${PRE} Ingestao"
airflow variables -i /conf__etl_oltp_2_raw.json

echo "${PRE} CONNECTIONS"
airflow connections -a --conn_id ${ALDATA__ENV__DAG_GIT} --conn_type http --conn_host "https://github.com/mdlabio/voz_digital.git" --conn_login woolong

echo "${PRE} Branch de Deploy"
airflow variables --set "${ALDATA__ENV__PROJECT_NAME}__deploy_git_branch" develop

echo "${PRE} VARIABLE AIRFLOW CONFIG DONE"
airflow variables --set aldata_airflow_config "done"

echo "${PRE} FINALIZADO"
echo "${HR}"
echo ""