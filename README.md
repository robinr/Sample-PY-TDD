# Sample-PY-TDD
A sample project in Python developed using TDD structure.

This project is an example of Python TDD sing Flask for web framework
and, to focus on testing, SQLite for database.

The app does the following.
o articles can be created
o articles can be fetched
o articles can be listed.

How to Use

1.  Clone the repo
2.  Then  cd blog_app
3.  Install the following
       - activate the venv using source bin/activate
       - pip install pytest && pip install "pydantic[email]"
       - pip install jsonschema Flask
       - pip install requests
       - pip install pytest-cov

How to Run and execute 

(venv)$ python -m pytest tests -m 'e2e'
(venv)$ python blog/init_db.py 
(venv)$ export PYTHONPATH=$PYTHONPATH:$PWD.
(venv)$ FLASK_APP=blog/app.py python -m flask run
(venv)$ python -m pytest tests -m 'not e2e'


       - 