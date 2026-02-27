from django.contrib import admin
from first_app.models import Employee
from first_app.models import Skill, Person, Department

# Register your models here.
admin.site.register(Employee)

class SkillAdmin(admin.ModelAdmin):
    search_fields = ['skill_name']

class PersonAdmin(admin.ModelAdmin):
    autocomplete_fields = ['skills']

admin.site.register(Skill, SkillAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Department)


# Email content
from django.contrib import admin
from .models import Emp
from .tasks import send_employee_mail

class EmpAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Call Celery task with 10 seconds delay
        send_employee_mail.apply_async(
            args=[
                obj.e_id,
                obj.e_name,
                str(obj.dept),
                obj.mobile,
                obj.hr_status,
                obj.admin_status
            ],
            countdown=10
        )

admin.site.register(Emp, EmpAdmin)