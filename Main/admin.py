from django.contrib import admin

# Register your models here.

from .models import Student, Cijfer, Toets, Blok

admin.site.register(Student)
admin.site.register(Cijfer)
admin.site.register(Toets)
admin.site.register(Blok)
