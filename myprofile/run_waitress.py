import os
from waitress import serve
from myprofile.wsgi import application

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myprofile.settings')
    serve(application, host='0.0.0.0', port=8000)

