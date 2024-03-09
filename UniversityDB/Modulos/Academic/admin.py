from django.contrib import admin
from Modulos.Academic.models import *

# Register your models here.
admin.site.register(Degree)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)