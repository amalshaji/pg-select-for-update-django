# Postgres select for update using django

## Install

```shell
virtualenv .venv
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
```

## Seed

```shell
python manage.py seed_data
```

## Start worker

```shell
python manage.py run_journey_creator
```
