import os
import time
import django,random as rd

os.environ.setdefault('DJANGO_SETTINGS_MODULE','biblioteca.settings')

django.setup()

from apps.libro.models import libro
