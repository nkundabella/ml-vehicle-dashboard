# Vehicle Machine Learning Dashboard

A Django dashboard that displays a one-way frequency table of vehicle
manufacturers from a CSV dataset.

## Requirements

- Python 3.10 or newer
- The dataset described below

## Setup

From the project directory, create and activate a virtual environment, then
install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate it with `source .venv/bin/activate`.

## Dataset

The app expects `dummy_data/vehicles_ml_dataset.csv` and reads its
`manufacturer` column. The dataset is deliberately excluded from Git because
it has client-related columns, including names, ages, locations, income, and
professions. Its source and redistribution permission have not been
established.

Before using or sharing a dataset, confirm that you have permission to use it
and that it contains no personal or confidential information that should not
be published. Obtain an appropriately licensed, synthetic, or anonymized
dataset and place it at the expected path. Do not commit the CSV unless its
contents and redistribution rights have been reviewed.

## Run locally

From the project directory, run:

```powershell
python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

Local development defaults to `DEBUG=True` and generates a temporary,
process-specific Django secret key if `DJANGO_SECRET_KEY` is not set. These
defaults are for local development only.

## Deployment configuration

Before deploying, set these environment variables in the hosting platform:

- `DJANGO_DEBUG=False`
- `DJANGO_SECRET_KEY` to a unique, securely generated secret
- `DJANGO_ALLOWED_HOSTS` to a comma-separated list of the actual hostnames,
  for example `dashboard.example.com`

Production startup fails if the secret key or allowed hosts are missing.
Never commit production secrets or put them in source control.
