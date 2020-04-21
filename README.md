# visiondemo
Django web app for vision algorithm demo.

Tested under: <br/>
Python version: 3.4.3 <br/>
Django version: 1.8.3


**Usage:**

`git clone https://github.com/charlesq34/visiondemo.git` <br/>
`cd visiondemo` <br/>

*[Optional]* <br/>
`virtualenv -p <python3_path> venv` <br/>
`source venv/bin/activate` <br/>
`pip install -r requirements.txt` <br/>

*[To start backend]* <br/>
`python manage.py runserver 8080` <br/>
`python visiondemo/external_app.py` <br/>

Go to http://127.0.0.1:8080/visiondemo

**Testing**

I created several test file inside the tests directory.

1. Start the backend first:

`python manage.py runserver 8080` <br/>
`python visiondemo/external_app.py` <br/>

2. Execute the test command:

`python manage.py test` <br/>


