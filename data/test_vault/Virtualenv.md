---
tags:
  - "#Python"
  - "#Dev"
links:
---
Одна из простейших [[Enviroments(python)]]

```bash
# Установка virtualenv
pip install virtualenv
# Создание окружения
virtualenv <env_name> -p python3.x
# Активация
source <env_name>/bin/activate  # Linux/macOS
<env_name>\Scripts\activate     # Windows
# Деактивация
deactivate
# Удаление
rm -rf <env_name>  # Linux/macOS
rmdir /s /q <env_name>  # Windows
# Установка зависимостей
pip install -r requirements.txt
```

Например дефолт
```bash 
virtualenv AlexGrad -p python3.10
source AlexGrad/bin/activate
pip install -r requirements.txt
```
