# Чат-бот для Поддержки Подростков "Подросток Al"

## Описание

Чат-бот **"Подросток Al"** предоставляет подросткам (13-17 лет) виртуальную психологическую поддержку на основе GigaChat от Сбер. Он помогает пользователям справляться с эмоциональными вызовами, трудностями в общении и саморазвитии, предлагая конкретные советы и техники управления эмоциями. Этот инструмент задуман как доступная альтернатива квалифицированной помощи, что особенно важно для подростков, сталкивающихся с географическими, финансовыми и стигматизационными барьерами при обращении к психологам.

## Продукт

Чат-бот "Подросток Al" умеет вести поддерживающие диалоги с демонстрацией эмпатии и понимания подростковых проблем. Он предоставляет:
- **Советы по эмоциональной регуляции**,
- **Методы преодоления стресса и тревоги**,
- **Ссылки на профессиональные ресурсы для дальнейшей поддержки**.

Дизайн веб приложения: [figma](https://www.figma.com/design/GTdHehucvIaE1bRBQGHR7h/КЕЙС-1?node-id=0-1)

## Структура проекта

- **app.py**: Главный файл приложения, реализующий маршруты и управление сессиями.
- **gigaChat.py**: Модуль, конфигурирующий подключение к GigaChat и обработку сообщений для чат-бота.

## Требования

- **Python 3.8+**
- **Flask** и **Flask-Session**
- **GigaChat API**: доступ к API GigaChat и учетные данные.

## Установка

1. **Склонируйте репозиторий**:
    ```bash
    git clone https://github.com/psihAI.git
    cd psihAI
    ```

2. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Настройте переменные среды**:
    Установите значения для `FLASK_SECRET_KEY` и `GIGACHAT_API_PERS`.

4. **Укажите безопасный путь для хранения сессий**:
    В `app.py` задайте значение `SESSION_FILE_DIR` на безопасный каталог на сервере.

## Описание файлов

### app.py

- **Маршруты**:
  - **`/` (index)**: Загружает интерфейс чата и отображает историю сообщений.
  - **`/chat`**: Принимает ввод пользователя через POST-запрос, отправляет на обработку и возвращает ответ чат-бота.
- **Управление сессиями**:
  - Безопасность сессий обеспечивается настройками: secure cookie, HTTP-only, SameSite, срок действия — 30 минут.

### gigaChat.py

- **Конфигурация**:
  - `gigaSystem` содержит набор инструкций, определяющих стиль общения бота.
  - `censor_and_paraphrase` контролирует чувствительный контент, предоставляя замещающие ответы при необходимости.
- **Функции**:
  - `answerGiga(system, topic)`: Отправляет сообщение на API GigaChat и получает ответ.
  - `censor_and_paraphrase(text)`: Проверяет сообщения на наличие определенных слов или фраз и, при необходимости, предлагает альтернативный ответ с рекомендацией обратиться за профессиональной помощью.

## Запуск приложения

1. **Запустите сервер**:
    ```bash
    python app.py
    ```
2. **Откройте приложение**:
   - Перейдите в браузере на `http://127.0.0.1:5000`, чтобы начать диалог с ботом.

## Конфиденциальность и безопасность

- **Переменные среды**: Держите в безопасности ключи, такие как `FLASK_SECRET_KEY` и `GIGACHAT_API_PERS`.
- **Безопасность сессий**: Использование `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SAMESITE` обеспечивает защиту пользовательских данных.

## Как использовать

- Перейдите на страницу приложения и введите сообщение в интерфейсе чата, чтобы начать общение.
- Сообщения проверяются на наличие запрещенных фраз. Если обнаружена чувствительная тема, бот предложит альтернативный ответ и рекомендации обратиться за профессиональной помощью.
