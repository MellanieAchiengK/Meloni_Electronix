# Melonie-Electronix
The objective of this project (Meloni Electronix) is to develop an e-commerce app for electronics business.

![CONTRIBUTING.md](/CONTRIBUTING.md)



create a databases

```
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
```

Create a environement virtual
```
cd Melanie_Electronix
python3 -m venv env
source env/bin/activate
```
install the dependence
```
pip install -r requirements.txt
```

```
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
ME_MYSQL_USER=melani_dev ME_MYSQL_PWD=Mel0ni_dev_123 ME_MYSQL_HOST=localhost ME_MYSQL_DB=ME_db python3 api/v1/app.py
curl http://127.0.0.1:5000/
http://127.0.0.1:5000/presentation
http://127.0.0.1:5000/api/v1/produit
```