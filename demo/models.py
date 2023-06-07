from django.db import models


class Project(models.Model):
    name = models.CharField(
        help_text="The name of the project",
        max_length=255,
    )


class Milestone(models.Model):
    name = models.CharField(
        max_length=255,
    )

    project = models.ForeignKey[Project](
        Project,
        on_delete=models.CASCADE,
        related_name="milestones",
        related_query_name="milestone",
    )

