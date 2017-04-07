# source setup.sh
pyvenv pyvenv
source pyvenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
