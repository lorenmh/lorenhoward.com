import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/loho')

if sys.version < "2.7.3": os.execl("/home/lorenmh/lorenhoward.com/env/bin/python", "python2.7.3", *sys.argv)

sys.path.insert(0,'/home/lorenmh/lorenhoward.com/env/bin')
sys.path.insert(0,'/home/lorenmh/lorenhoward.com/env/lib/python2.7/site-packages/django')
sys.path.insert(0,'/home/lorenmh/lorenhoward.com/env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "loho.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()




