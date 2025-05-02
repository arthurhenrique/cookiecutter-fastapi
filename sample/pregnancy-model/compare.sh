#!/bin/bash

idade_mae=$1
horas_sono=$2
alimentacao_saudavel=$3
nivel_estresse=$4
atividade_fisica_semana=$5
renda_familiar=$6
apoio_social=$7

if [ $# -ne 7 ]; then
  echo "uso: $0 <idade_mae> <horas_sono> <alimentacao_saudavel> <nivel_estresse> <atividade_fisica_semana> <renda_familiar> <apoio_social>"
  exit 1
fi

echo "pregnancy-model forest"
curl -s -w "time_total: %{time_total}s\n" -X 'POST' \
  'http://0.0.0.0:8080/api/v1/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "{
  \"idade_mae\": $idade_mae,
  \"horas_sono\": $horas_sono,
  \"alimentacao_saudavel\": $alimentacao_saudavel,
  \"nivel_estresse\": $nivel_estresse,
  \"atividade_fisica_semana\": $atividade_fisica_semana,
  \"renda_familiar\": $renda_familiar,
  \"apoio_social\": $apoio_social
}"

echo "------------------"
prompt="bem-estar da grávida: idade_mae $idade_mae, horas_sono $horas_sono, alimentacao $alimentacao_saudavel, estresse $nivel_estresse, atividade $atividade_fisica_semana, renda $renda_familiar, apoio $apoio_social. seja sucinto e responda somente com bem-estar: positivo ou bem-estar: negativo?"

model="gpt-3.5-turbo"  # ou gpt-4 se preferir
echo "open ai $model"
curl -s -w "time_total: %{time_total}s\n" https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d "{
    \"model\": \"$model\",
    \"messages\": [{\"role\": \"user\", \"content\": \"$prompt\"}]
  }"