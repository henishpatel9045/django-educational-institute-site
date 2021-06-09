from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.detail)
admin.site.register(models.course)
admin.site.register(models.facultie)
admin.site.register(models.students_review)
admin.site.register(models.image)
admin.site.register(models.PeolpeContactUs)
admin.site.register(models.People_Request_For_Call)
admin.site.register(models.AboutUs)