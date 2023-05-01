# Тестовое задание для Rekruto
## Описание задания
Создать URL с query параметрами name и message.
## Стек
1) Python 3.11
2) Django 4.2
## Установка
```bash
git clone git@github.com:RG1ee/rekruto-test.git
cd rekruto-test

# Cкопируйте образец среды в `.env` и измените значения
cat env_sample > .env
```

## Разработка
```bash
python3.11 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install
# Необязательно
rekruto migrate
```

## Запуск сервера
```bash
rekruto runserver
```
## Перейти на locallhost
http://localhost:8000/?name=rekruto&message=Давай%20дружить!
