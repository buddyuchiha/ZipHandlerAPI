# Zip Handler API

Микросервис для проверки содержимого ZIP-архивов с хранением в MinIO и аутентификацией через Keycloak.

[Техническое задание](https://github.com/user-attachments/files/23812730/zip.pdf)

## Функционал

* Загрузка архивов: Прием ZIP-архивов до 100 МБ с проверкой целостности
* Аутентификация и авторизация: Безопасный доступ через Keycloak OAuth2
* Хранение файлов: Надежное хранение в MinIO object storage
* Валидация: Проверка целостности архивов, валидация формата и размера
* REST API: Полное API на FastAPI с автоматической документацией OpenAPI

## Технологии

![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/-Alembic-00A98F?logo=alembic&logoColor=white)
![Pydantic](https://img.shields.io/badge/-Pydantic-E92063?logo=pydantic&logoColor=white)
![Keycloak](https://img.shields.io/badge/-Keycloak-2C7FBF?logo=keycloak&logoColor=white)
![MinIO](https://img.shields.io/badge/-MinIO-8C4B31?logo=minio&logoColor=white)

## Инструкция запуска через Docker Compose

1) Клонировать git-репозиторий

<img width="845" height="404" alt="image" src="https://github.com/user-attachments/assets/163af613-1696-4c66-95cb-a7cb855f38d1" />

<img width="954" height="190" alt="image" src="https://github.com/user-attachments/assets/092018ef-be4f-4645-8793-eb17d6ad002a" />

2) Открыть проект

<img width="664" height="51" alt="image" src="https://github.com/user-attachments/assets/4a2fe983-649e-4d28-87b7-a1cc54a56874" />

3) Сконфигурировать .env по шаблону

<img width="1563" height="625" alt="image" src="https://github.com/user-attachments/assets/f11dd11b-2481-41fc-9e12-67d45d70f2cf" />

4) Выполнить команду docker compose up -d --build

<img width="554" height="27" alt="image" src="https://github.com/user-attachments/assets/aad17934-130c-4070-8856-d91438900e96" />

<img width="423" height="123" alt="image" src="https://github.com/user-attachments/assets/cd1b0b7c-fd58-4f86-a171-0f64abab7618" />

5) Подождать 20 секунд и перейти на: http://127.0.0.1:8000/docs

<img width="1807" height="870" alt="image" src="https://github.com/user-attachments/assets/70860276-1de5-4f69-bdca-a3793bb3ba34" />

## Инструкция локального запуска

1) Клонировать git-репозиторий

<img width="845" height="404" alt="image" src="https://github.com/user-attachments/assets/163af613-1696-4c66-95cb-a7cb855f38d1" />

<img width="954" height="190" alt="image" src="https://github.com/user-attachments/assets/092018ef-be4f-4645-8793-eb17d6ad002a" />

2) Открыть проект

<img width="664" height="51" alt="image" src="https://github.com/user-attachments/assets/4a2fe983-649e-4d28-87b7-a1cc54a56874" />

3) Сконфигурировать .env по шаблону

<img width="1563" height="625" alt="image" src="https://github.com/user-attachments/assets/f11dd11b-2481-41fc-9e12-67d45d70f2cf" />

4) Активировать виртуальное окружение и установить зависимости

<img width="657" height="62" alt="image" src="https://github.com/user-attachments/assets/81f6444b-59de-462b-994d-d77026383a4b" />

5) Выполнить команду docker compose up -d postgres_app postgres_keycloak minio keycloak

<img width="847" height="29" alt="image" src="https://github.com/user-attachments/assets/e2c9d6c7-f0c1-44e4-95da-93c297163885" />

6) Выполнить команду python src/main.py и перейти на http://127.0.0.1:8000/docs

<img width="787" height="114" alt="image" src="https://github.com/user-attachments/assets/7c43dee9-a0f6-4dac-aa17-b3facc472c2b" />

<img width="1827" height="877" alt="image" src="https://github.com/user-attachments/assets/a1c34568-7ff1-4b64-9883-de72e2c3ba09" />

## Авторизация

1) Нажать на кнопку

<img width="371" height="276" alt="image" src="https://github.com/user-attachments/assets/75db0719-9676-4dc9-9e0b-351a1f2471c8" />

2) В появившемся окне вставить client_id и client_sercret, значения которых можно взять из .env-template

<img width="514" height="364" alt="image" src="https://github.com/user-attachments/assets/1b60493c-0a2c-4779-acaf-dd24b431bd9d" />

<img width="365" height="42" alt="image" src="https://github.com/user-attachments/assets/8d5446ee-69bc-418c-b212-db6fa7410bfa" />

3) Войти в тестовый аккаунт пользователя, значение которого можно взять из keycloak_setup/keycloak_setup.json

<img width="598" height="435" alt="image" src="https://github.com/user-attachments/assets/aa2cdc02-d3af-4521-a50d-6e924d7367f7" />

<img width="401" height="244" alt="image" src="https://github.com/user-attachments/assets/eacca052-5900-464f-996e-7661f20428f5" />

4) После появится возможность использовать эндпоинты

<img width="1298" height="854" alt="image" src="https://github.com/user-attachments/assets/8582e28c-7f56-4a45-a935-40832505f237" />

## Админ панели

Minio: http://127.0.0.1:9001/login
Пароль и логин: minioadmin

<img width="230" height="41" alt="image" src="https://github.com/user-attachments/assets/281e635d-fd72-4d00-809d-71ac14b2fe28" />

Keycloak: http://localhost:8080
Пароль и логин: admin

<img width="253" height="40" alt="image" src="https://github.com/user-attachments/assets/61946965-cb1d-4705-b800-bd36fd14ad4a" />

