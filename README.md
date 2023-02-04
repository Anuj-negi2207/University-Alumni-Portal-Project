# **UNIVERSITY ALUMNI PORTAL PROJECT**

>## DESCRIPTION
The objective of this application is to allow old and new students of a university or college to communicate with each other. This system allows students to know about each other and their current activities and work forward towards their own goals by the guidance of their college's alumni. 

>## FRAMEWORK
Any web technology can be used but we're using DJANGO Framework.


>## GETTING STARTED

=> **Fork <a href=https://github.com/Anuj-negi2207/University-Alumni-Portal-Project><img src="https://img.icons8.com/ios/24/000000/code-fork.png"></a>this repository to start contributing.**

=> Open your Git Bash command window and in the root directory type the following commands :
```bash
    1) git init -initializes the git repository from the GitHub. 
    2) git clone -Clone the repository to your local machine
      (git clone https://github.com/Anuj-negi2207/University-Alumni-Portal-Project.git)
``` 

Installation
------------

Install `pip` and then install system-wide `virtualenv` PIP package.

    sudo apt-get install python-pip
    sudo pip install virtualenv

Create a virtual environment for our current `university-alumni-portal-project` project in a
folder named `.venv`, and "activate" it, so that all our subsequent PIP
packages are installed in this virtual environment only, and not globally. Note
that you don't require `sudo` access any more to install PIP packages in this
local virtual environment.

    cd alumni-portal
    virtualenv .venv
    source .venv/bin/activate


Install the dependencies using:

    pip install -r requirements.txt

**Note:** Above command installs Django also.

Running the Django app
----------------------

Create SQLite database, which is just a file `db.sqlite3` being used as
database for this app.

    python manage.py migrate

And then run the Django app

    python manage.py runserver

Now you can go to your browser and type `http://127.0.0.1:8000/` and you can
see the Django app in action!
