#!/bin/bash

echo "Tipos disponíveis:"
options=("feat" "fix" "docs" "style" "refactor" "test" "chore" "revert")

# Valida se recebeu mensagem
if [ -z "$1" ]; then
  echo "❌ Você precisa passar uma mensagem de commit."
  echo "Exemplo:"
  echo "   make commit m=\"feat(api): adiciona endpoint de healthcheck\""
  exit 1
fi

select opt in "${options[@]}"
do
  if [[ -n "$opt" ]]; then
    git commit -m "$opt: $*"
    break
  else
    echo "Opção inválida!"
  fi
done
