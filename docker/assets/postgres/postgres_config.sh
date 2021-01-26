#!/usr/bin/env bash

: "${FERNET_KEY:=${AIRFLOW__CORE__FERNET_KEY}}"

HR="***********************************************************************************"
PRE="-----------------"

echo
echo "${HR}"
echo "* Projeto: ${ALDATA__ENV__PROJECT_NAME}"
echo "* ** Realiza configuracoes basicas do postgres"
echo "* ** Esse script roda apenas uma vez e eh deletado apos execucao pelo /entrypoint.sh"
echo "${HR}"
echo ''

echo "${PRE} Databases"

echo '${PRE}${PRE} Banco de Dados - Postgres - STAGE'
createdb VOZ_STAGE

echo '${PRE}${PRE} Banco de Dados - Postgres - DW'
createdb VOZ_STAGE


echo "${PRE} FINALIZADO"
echo "${HR}"
echo ''
