import os, argparse
from selenium import webdriver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CEC.settings')

import django
django.setup()

from courses.models import Course, Teacher, Criteria

browser = webdriver.Firefox()


def get_userpass():
	"""
	Get Username and Password User entered into Command Line
	Returns parser
	"""
	parser = argparse.ArgumentParser(description='WebLogin to UW')
	parser.add_argument('username')
	parser.add_argument('password')

	return parser.parse_args()

def login(user_input):
	"""
	Logs into WebLogin UW
	Username and Password given work
	Pass in Selenium browser to be in the same session
	"""
	browser.get('https://weblogin.washington.edu')
	loginElement = browser.find_element_by_id('weblogin_netid')
	loginElement.send_keys(user_input.username)

	passwordElement = browser.find_element_by_id('weblogin_password')
	passwordElement.send_keys(user_input.password)
	passwordElement.submit()

def read_file():
	"""
	Read the file containing all the links to Course Evals
	"""

	global COURSE_LINKS
	COURSE_LINKS = [line.rstrip('\n') for line in open('..//CourseEvalRetriever//testLinks.txt')]


def extract_data(url):
	"""
	Get the Course Information from given course website.
	"""
	browser.get(url)
	
	try:
		WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
	finally:
		browser.quit()

	course_name = browser.find_element_by_tag_name('h1').text
	teacher_name = browser.find_element_by_tag_name('h2').text
	course_info = browser.find_element_by_tag_name('table').text

	with open('output.txt', 'a') as f:
		f.write(course_name + '\n')
		f.write(teacher_name + '\n')
		f.write(course_info + '\n\n')
def parse_course_name(course):

def parse_teacher_name(teacher):
	"""
	returns array where information is stored in the following order
	teacher name, standing, quarter
	"""
	teacher_name = " "." ".join(teacher.split()[0:2])

	return teacher_name
def parse_course_info(info):

def main():
	login(get_userpass())
	read_file()

	for link in COURSE_LINKS:
		extract_data(link)


	browser.quit()	
	print("Done")	

if __name__ == '__main__':
	print("Starting CEC population script...")
	main()
	