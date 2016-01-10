from django.contrib import admin
from .models import Course, Teacher, Criteria

class CriteriaInLine(admin.StackedInline):
	model = Criteria

class TeacherInLine(admin.StackedInline):
	model = Teacher
	extra = 0

	inlines = [CriteriaInLine]


class CourseAdmin(admin.ModelAdmin):
	fieldsets = [
    	(None,               {'fields': ['department']}),
    	('Course Information', {'fields': ['course_id']}),
	]
	inlines = [TeacherInLine]

class TeacherAdmin(admin.ModelAdmin):
	inlines = [CriteriaInLine]


admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)