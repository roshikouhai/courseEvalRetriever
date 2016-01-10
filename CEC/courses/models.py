from django.db import models

class Course(models.Model):
	department = models.CharField(max_length=260)
	course_name = models.CharField(max_length=260)

	# Add in date updated. 
	def __str__(self):
			return self.department + ' ' + self.course_name

	""" 
	Add function to other script
	def breakdown_course(course):
		
		Splits the full course name into course name, teacher, quarter
		taught and course id.
		COULD MAKE BETTER USING SPLIT()
		

		#Get department by going through string until its only a title
		i = 0 
		while i < len(course) and not course[:-i].isTitle():
			i = i +1

		department = course[:-i-2]
		other_part = course[len(department) +1 :]

		# Get course name and number by iterating through string until its 
		# comprised off all uppercases and numbers.
		i = 1
		while i < len(other_part) and other_part[:i].isupper():
			i = i +1
		course_name = other_part[:i-2].strip()

		# Retrieve teacher name and standing.
		other_part = other_part[len(course_name) + 1:].strip()

		quarter = other_part[-4:]
		other_part = other_part[:-4].strip()

		teacher = ' '.join(other_part.split()[:2])
		standing = ' '.join(other_part.split()[2:])

		return (department, course_name, teacher, standing, quarter)

	"""
class Teacher(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE, verbose_name = "Teacher who taught course")
	teacher = models.CharField(max_length=40)
	standing = models.CharField(max_length=30)
	quarter = models.CharField(max_length=4)
	surveyed = models.IntegerField()
	enrolled = models.IntegerField()
	lecture_form = models.CharField(max_length=30)

	def __str__(self):
		return self.teacher + ' ' + self.quarter
		
class Criteria(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, verbose_name = "Teacher Evaluations")
	CRITERIA_CHOICES = (
		('whole', 'Course as a whole'),
		('txtbk_oa', 'Textbook Overall'),
		('instr_oa', 'Instructor Overall'),
		('c_content', 'Course Content'),
		('instr_contrib', "Instructor's Contribution"),
		('instr_effect', "Instructor's Effectiveness"),
		('instr_interest', "Instructor's Interest"),
		('amt_learned', 'Amount learned'),
		('grading_tech', 'Grading Techniques'),
		('relev_of_hw', 'Relevance and usefulness of homework'),
	)
	criteria = models.CharField(max_length = 20, choices = CRITERIA_CHOICES)
	excellent = models.IntegerField()
	very_good = models.IntegerField()
	good = models.IntegerField()
	fair = models.IntegerField()
	poor = models.IntegerField()
	very_poor = models.IntegerField()
	median = models.DecimalField(max_digits= 3, decimal_places = 2)

	def __str__(self):
		return self.criteria + ' '+ self.median
