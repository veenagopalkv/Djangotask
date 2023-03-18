from django.contrib import admin
from .models import Department,Course,person
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','seats','available_seats']
    list_editable = ['seats','available_seats']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    
admin.site.register(Course,CourseAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'Date_of_birth', 'mail_id','Age','phone_number']
    list_editable = ['mail_id', 'Age','phone_number']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(person, PersonAdmin)

