#!/bin/bash

# Navega até o diretório do frontend e instala as dependências
cd google-cryptocurrency/frontend
npm install

# Constrói o frontend
npm run build

# Retorna ao diretório raiz
cd ..

# Inicia o servidor Uvicorn
cd backend
echo "Rodando na porta: $PORT"
uvicorn main:app --host 0.0.0.0 --port $PORT
