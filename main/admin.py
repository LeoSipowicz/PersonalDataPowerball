from django.contrib import admin
from .models import PersonalDataModel

# Register your models here.


@admin.register(PersonalDataModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    PersonalDataModel._meta.get_fields()]
