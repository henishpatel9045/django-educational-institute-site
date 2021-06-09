from django.contrib import admin
from . import models
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor')


class FacultieAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


class StudentReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'time_of_creation')
    

class RequestCallAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone', 'city', 'time_of_creation')


admin.site.register(models.detail)
admin.site.register(models.course, CourseAdmin)
admin.site.register(models.facultie, FacultieAdmin)
admin.site.register(models.students_review, StudentReviewAdmin)
admin.site.register(models.image)
admin.site.register(models.PeolpeContactUs, ContactUsAdmin)
admin.site.register(models.People_Request_For_Call, RequestCallAdmin)
admin.site.register(models.AboutUs)

admin.site.site_header = "Sigma Classes"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Welcome To Sigma Classes Dashboard."
# admin.site.login_template = 
