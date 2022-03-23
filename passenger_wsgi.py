import os
import sys
from urllib.parse import unquote

from django.core.wsgi import get_wsgi_application
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL) 


sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "clever.settings.prod" 
def application(environ, start_response):
    environ["PATH_INFO"] = unquote(environ["PATH_INFO"]).encode('utf-8').decode('iso-8859-1')
    _application = get_wsgi_application()
    return _application(environ, start_response)

