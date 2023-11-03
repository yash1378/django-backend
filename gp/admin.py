from django.contrib import admin
from .models import Student, Mentor,Owner,MentorCred,RenrollData

# Register your models here.
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Owner)
admin.site.register(MentorCred)
admin.site.register(RenrollData)

