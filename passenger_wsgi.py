# passenger_wsgi.py

import os
import sys

# Add project path
sys.path.insert(0, "/home/hightech/project1.hornetspestcontrols.com/service")

# Activate virtualenv
activate_env = "/home/hightech/virtualenv/project1.hornetspestcontrols.com/service/3.10/bin/activate_this.py"

with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()