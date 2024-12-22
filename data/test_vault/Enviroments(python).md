---
Связи: "[[Python]]"
tags:
  - "#Dev"
  - "#Python"
links:
---
Энвайроменты - одна из основных сущностей в питоне
Позволяют создать (отноительно) независимое окружение под проект


## [[Conda]]
Используется для создание env и переключения. Имеет свой пакетный манагер-установщик, но я предпочитаю пип. Читшит https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html
Основные команды:
	conda info
	conda create -n ENVNAME python=3.10
	conda env list
	conda activate ENVNAME


## Pip

pip install -r requirements.txt


[[Virtualenv]]
```bash 
virtualenv AlexGrad -p python3.10
source AlexGrad/bin/activate
pip install -r requirements.txt
```