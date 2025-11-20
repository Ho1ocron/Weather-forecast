# UrFU homework

A simple weather forecast website made with **Django** and **Open-Meteo** for the my home assignment.

## Python set-up

1. Clone the repo

    ```bash
    git clone https://github.com/Ho1ocron/Weather-forecast.git
    cd Weather-forecast
    ```

2. Create and set-up virtual environment

    - For Linux / MacOS

        ```bash
        python3 -m venv .venv
        source ./.venv/bin/activate
        ```

    - For Windows

        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Django project

1. Starting the project

    ```bash
    django-admin startproject project
    ```

2. Creating an app within the project (Optional for this project)

    ```bash
    python project/manage.py startapp myapp
    ```

3. Starting the server

    ```bash
    python manage.py runserver
    ```
