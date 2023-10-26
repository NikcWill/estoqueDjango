--configurando ambiente--

python -m venv venv

python .\venv\Scripts\activate

pip install django

pip freeze > requirements.txt

pip install -r requirements.txt

-- inicar o projeto -- 

python -m django startproject NOME_DO_PROJETO .
python manage.py startapp NOME_DO_APP

python manage.py makemigrations
python manage.py migrate

--criando super usuario--

python manage.py createsuperuser

python manage.py shell##

python manage.py runserver
