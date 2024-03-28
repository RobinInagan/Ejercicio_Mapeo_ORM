from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=["name","init_date","end_date"]

class TaskAdmin(admin.ModelAdmin):
    list_display=["id","project","description","priority"]

class CommentAdmin(admin.ModelAdmin):
    list_display=["id","task","content","init_date"]

class OwnerAdmin(admin.ModelAdmin):
    list_display=["task","user"]

class MemberAdmin(admin.ModelAdmin):
    list_display=["rol","date"]

admin.site.register(Project,ProjectAdmin)
admin.site.register(Tasks,TaskAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Owners,OwnerAdmin)
admin.site.register(Members,MemberAdmin)

