from django.contrib import admin

from . import models




######### TASK ADMIN #########
@admin.register(models.Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ["id","user","title", "description", "background_image", "hackathon_image", "submission_type", "start_datetime", "end_datetime", "reward_prize"]
    list_filter = []

######### USER ADMIN #########
@admin.register(models.User)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','mail_id']
    list_filter = []

######### REGISTER ADMIN #########
@admin.register(models.Register)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['user','hackathon','is_available']
    list_filter = []

@admin.register(models.Submission)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title","user","summary","hackathon","image", "file", "link","github_link","other_link","is_favourite","sub_date"]
    list_filter = []
