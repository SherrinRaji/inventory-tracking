# Steps to make this repo work :)

Prerequisite: You will have to have Python and pip already installed. Check out below links for installation.

https://www.python.org/downloads/

https://pip.pypa.io/en/stable/installation/

## 1. Clone this Repository
## 2. Create Virtual Environment
```
python3 -m venv venv
```
```
source venv/bin/activate
```

## 3. Upgrade 
```
pip install --upgrade pip
```
## 4. Install packages in requirements.txt
```
pip install -r requirements.txt
```
```
export FLASK_APP=crudapp.py
```

## 5. Flask set-up
```
flask db init
```
```
flask db migrate -m "entries table"
```
```
flask db upgrade
```
## 6. Run the app
```
flask run
```