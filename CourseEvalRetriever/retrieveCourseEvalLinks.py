#TODO: Add functionality to save location, spot to resume download
#TODO: Set up how to download information
#TODO: Set up log file.
#TODO: Upload to online database.
"""
Web Page Scraper for Teacher Evals Page
github/mikur/mikurio
Only goes through to find the links. 
"""

import os, argparse, string
from selenium import webdriver

course_links =[]
browser = webdriver.Firefox()

def set_up_directory(directory):
	"""
	Place to download all the data
	Will change in the future as we determine database
	"""
	os.chdir(directory)

def clean_links(links):
	"""
	Remove links that don't link to teacher evals
	Add in the extension.
	"""
	return [webelement.get_attribute('href') for webelement in links[9:-3]]

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

def get_all_course_links(url):
	"""
	Open a page listing all courses and retrieve all the teacher links
	"""

	browser.get(url)
	return clean_links(browser.find_elements_by_tag_name('a'))

def log_links(links):
	"""
	Saves all the links to a text file.
	"""
	
	with open('CourseEvalLinks.txt', 'w') as f:
		for url in links:
			f.write(url + '\n')

	print('Done saving')

			
def main():
	set_up_directory("C:\\Users\\Leo\\Envs\\courseEvalRetriever\\courseEvalRetriever\\CourseEvalRetriever")
	
	login(get_userpass())
	
	list_of_sites = ['https://www.washington.edu/cec/{0}-toc.html'.format(s) 				for s in string.ascii_lowercase[:23]]

	# Traverse Courses A-W
	for url in list_of_sites:
		course_links.extend(get_all_course_links(url))
		print('Done with {}'.format(url))
		
	log_links(course_links)	

	browser.quit()	
	print("Done")	

if __name__ == '__main__':
	main()
