#!/bin/bash

# Navega até o diretório do frontend e instala as dependências
cd frontend
npm install

# Constrói o frontend
npm run build

# Retorna ao diretório raiz
cd ..

# Navega até o diretório do backend e instala as dependências
cd backend
pip install -r requirements.txt

# Inicia o servidor Uvicorn
uvicorn main:app --host 0.0.0.0 --port $PORT
