from django.contrib import admin
from .models import Utilisateur,Task,Project,Comment,Deadline

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Deadline)