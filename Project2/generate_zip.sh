#!/bin/bash

# Cria o diretório entrega
mkdir entrega

# Copia os diretórios app e data para dentro de entrega
cp -r ./app ./entrega
cp -r ./data ./entrega

# Remove o arquivo gerador.py dentro de entrega/data
rm -f ./entrega/data/gerador.py

# Copia o arquivo E2-report-69.ipynb para dentro de entrega
cp E2-report-69.ipynb ./entrega

# Remove o arquivo zip antigo, se existir
rm -f entrega-bd-02-69.zip

# Cria o arquivo zip sem incluir o diretório entrega
cd entrega
zip -r ../entrega-bd-02-69.zip ./*
cd ..

# Remove o diretório entrega e todo o seu conteúdo
rm -rf entrega
