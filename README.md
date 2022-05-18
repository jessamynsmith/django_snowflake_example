# django_snowflake_example

This is an example of reading data from Snowflake and displaying it in a Django view.

### Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/django_snowflake_example.git
    
Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX).
NOTE! You must change 'path/to/python3' to be the actual path to python3 on your system. Make sure you are in the project directory (with manage.py) when you run the following:

    /path/to/python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Edit settings.py to include your Snowflake connection info under DATABASES.

Set up db:

    python manage.py migrate

Run server:

    python manage.py runserver
