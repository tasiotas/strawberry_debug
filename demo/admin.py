from django.contrib import admin
from .models import Milestone, Project


class MilestoneAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Project, ProjectAdmin)