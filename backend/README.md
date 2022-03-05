# Backend

Got to backend folder

```
cd backend
```

## Project setup

Create a virtual environment (recommended).

```
conda create -n backend-env python=3.8
canda activate backend-env
```

Install needed requirements from the requirements.txt file

```
pip install -r backend/requirements.txt
```

### Compile and make necessary migrations

```
python manage.py makemigrations
python manage.py migrate
```

### Run the backend

```
python manage.py runserver
```
