# Тестовый проект Django Stripe API

Тестовый проект Django Stripe API

![workflow](https://github.com/ShamievDima/test-stripe-project/actions/workflows/test_workflow.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

Проект создан с целью ознакомиться с платёжной системой Stripe.com. Она имеет подробный API и бесплатный тестовый режим для имитации
и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные
клиента, и реализовывать прочие платежные функции.
Существует несколько [тестовых карт](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout&integration=checkout#additional-testing-resources)
(4242 4242 4242 4242 - для проведения успешного платежа),
которые вы можете использовать, чтобы проверить работу приложения. Используйте их с любым CVC и сроком действия карты.

## Реализованные задачи

- Django Модели Item, Order, Discount, Tax
- Просмотр Django Моделей через Django Admin панели
- Использование environment variables
- Запуск используя Docker
- Stripe Payment Intent
- Запуск приложения на удаленном сервере, доступном для тестирования

## Установка

Склонируйте репозиторий. Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`, активируйте его (Windows: `source venv\scripts\activate`; Linux/Mac: `source venv/bin/activate`), установите зависимости `python -m pip install -r requirements.txt`.
Переименуйте `.env.example` в `.env`  и заполните его.

Для запуска сервера разработки, находясь в директории проекта выполните команды:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Запуск проекта

Перейдите в папку проекта и выполните команду:

```
docker-compose up -d --build
```

При первом запуске для функционирования проекта выполните команды:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

## Деплой на удаленный сервер

Необходимо создать переменные окружения в вашем репозитории github в разделе `secrets`

```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь сервера
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта (для оправки уведомления об успешном деплое)
TELEGRAM_TOKEN # Токен бота (для оправки уведомления об успешном деплое)
STRIPE_PUBLISHABLE_KEY # Ваш Publishable key с сайта stripe.com
STRIPE_SECRET_KEY # Ваш Secret key с сайта stripe.com
```

При каждом обновлении репозитория (git push) будет происходить:

- проверка кода соответствие страндарту PEP8 (с помощью пакета flake8)
- сборка и обновление образа на сервисе Docker Hub
- автоматический деплой на сервер, указанный в secrets
- отправка уведомления в Telegram

## URL адреса

| *URL* | *Метод*|*Описание*|
|-------|--------|----------|
| `api/buy/{id}` | `GET` | создает Stripe PaymentIndent для Item и возвращает __user_secret__|

Success Response:

- Code: 200
- Content:

```
{"client_secret": "some_secret_key"}
```

| *URL* | *Метод*|*Описание*|
|-------|--------|-------------|
| `api/item/{id}` | `GET` | возвращает страницу выбранного item и форму для оплаты картой через Stripe |

Success Response:

- Code: 200
- Content:Checkout page

| *URL* | *Метод*|*Описание*|
|-------|--------|----------|
| `api/buy-order/{id}` | `GET` | создает Stripe PaymentIndent для Order и возвращает __user_secret__|

Success Response:

- Code: 200
- Content:

```
{"client_secret": "some_secret_key"}
```

| *URL* | *Метод*|*Описание*|
|-------|--------|-------------|
| `api/order/{id}` | `GET` | возвращает страницу выбранного order и форму для оплаты картой через Stripe |

Success Response:

- Code: 200
- Content:Checkout page

## Об авторе

Ирина Фок [iricshkin](https://github.com/iricshkin/)
