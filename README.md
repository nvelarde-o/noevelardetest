# Noe Velarde-Test

## Installation

Put the `.env` file in the same directoy as `manage.py`

Create a virtual environment

```bash
  python -m venv /path/to/new/virtual/environment
```
Activate the venv
```bash
  source venv/bin/activate
```
Install the required packages from the requirements.txt file
```bash
  pip install -r /path/to/requirements.txt
```
Run migrations
```bash
  python manage.py migrate
```
Run the project
```bash
  python manage.py runserver
```

## How to test the API

1. Send a POST request to `http://127.0.0.1:8000/api/create-short-url/` with the key `url` and the original URL as value (ex. `https://google.com`) as form-data.
2. The new short URL will be returned:
   ```
   {
    "short_url": "http://127.0.0.1:8000/short-url/gyizowrgqi"
   }
   ```
3. Open the short url returned and it will redirect to the original url.

## Get most visited URL's

1. Send a GET request to `http://127.0.0.1:8000/api/get-top-100-urls/`, an array with the top 100 most visited sites will be returned.

## Running the Cronjob

Run the cronjob to update the url objects titles:
`python manage.py crontab add`
