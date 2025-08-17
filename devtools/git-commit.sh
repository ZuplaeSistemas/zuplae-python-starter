#!/bin/bash

echo "Tipos disponíveis:"
options=("feat" "fix" "docs" "style" "refactor" "test" "chore" "revert")

# Valida se recebeu mensagem
if [ -z "$1" ]; then
  echo "❌ Você precisa passar uma mensagem de commit."
  echo "Exemplo:"
  echo "   make commit m=\"adiciona endpoint de healthcheck\""
  exit 1
fi

# Lista de escopos comuns
scopes=("api" "ci" "docker" "tests" "config" "db")

echo "Selecione o escopo ou digite um personalizado:"
select scope in "${scopes[@]}" "Outro"
do
  if [[ -n "$scope" ]]; then
    if [[ "$scope" == "Outro" ]]; then
      echo "Digite o escopo desejado:"
      read scope
    fi
    if [[ -z "$scope" ]]; then
      echo "❌ O escopo não pode ser vazio."
      exit 1
    fi
    break
  else
    echo "Opção inválida!"
  fi
done

# Seleciona o tipo
select opt in "${options[@]}"
do
  if [[ -n "$opt" ]]; then
    # Monta no formato Conventional Commits
    git commit --amend -m "$opt($scope): $*"
    echo "✅ Commit atualizado: $opt($scope): $*"
    break
  else
    echo "Opção inválida!"
  fi
done
