# GitHub API Test

1. Создайте и активируйте виртуальное окружение:

    ```
    python -m venv venv
    ```

    Для mac/linux
    ```
    source venv/bin/activate
    ```
    
    Для Windows
    ```
   venv\Scripts\activate
    ```

1. Установите зависимости:

    ```
    pip install -r requirements.txt
    ```

2. Настройка переменных окружения

    Создайте файл `.env` в корне проекта и добавьте в него следующие строки:
    ```
    GITHUB_USERNAME=your_username
    GITHUB_TOKEN=your_token
    REPO_NAME=test-repo
    ```
    Замените `your_username`, `your_token` и `test-repo` на свои значения.

3. Запуск теста

    Выполните скрипт `test-api.py`:

    ```
    python test-api.py
    ```

Эти шаги создадут полностью рабочий проект для тестирования GitHub API. Убедитесь, что у вас есть активный токен GitHub API и права на создание и удаление репозиториев.
