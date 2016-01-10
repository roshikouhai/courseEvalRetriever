import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CEC.settings')

import django
django.setup()

from courses.models import Course, Teacher, Criteria

