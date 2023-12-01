# cadastre

## Description

The django-cadastre-api is a Django application that provides an API for working with cadastral data. The project includes endpoints for sending queries, getting results, pinging the server, and viewing query history.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DOGERAZ/django-cadastre-api
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    .\venv\Scripts\activate   # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add the secret key:

    ```plaintext
    DJANGO_SECRET_KEY=mysecretkey
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Sending a query:

    Send a POST request to the `/query/` endpoint with data in JSON format, for example:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"cadastre number": "12345", "latitude": "40.7128", "longitude": "-74.0060"}' http://localhost:8000/query/
    ```

2. Getting the result:

    Send a GET request to the `/result/` endpoint:

    ```bash
    curl http://localhost:8000/result/
    ```

3. Pinging the server:

    Send a GET request to the `/ping/` endpoint:

    ```bash
    curl http://localhost:8000/ping/
    ```

4. Viewing query history:

    Send a GET request to the `/history/` endpoint:

    ```bash
    curl http://localhost:8000/history/
    ```

## Additional Settings

- Project settings are located in the `cadastre/settings.py` file.
- For security, use environment variables to configure the secret key and other confidential data.

## Security

- Do not include secret files and keys in the repository.
- Check and update dependencies to prevent vulnerabilities.

