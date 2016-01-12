import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CEC.settings')

import django
django.setup()

from courses.models import Course, Teacher, Criteria

def populate():







if __name = '__main__':
	print "Starting CEC population script..."
	populate()
	