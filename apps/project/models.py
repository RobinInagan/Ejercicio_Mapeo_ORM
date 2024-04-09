from django.db import models

from apps.users.models import Users

class Project(models.Model):
    name = models.CharField(max_length = 60)
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

class Tasks(models.Model):
    description = models.CharField(max_length = 250)
    end_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete = models.DO_NOTHING)
    priority_choices = (
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
    )
    priority = models.CharField(max_length = 6,choices = priority_choices, default = 3)

class Comments(models.Model):
    user = models.ForeignKey(Users,on_delete = models.DO_NOTHING)
    task = models.ForeignKey(Tasks,on_delete = models.DO_NOTHING)
    init_date = models.DateTimeField()
    content = models.CharField(max_length = 120)

class Owners(models.Model):
    user = models.ForeignKey(Users,on_delete = models.DO_NOTHING)
    task = models.ForeignKey(Tasks,on_delete = models.DO_NOTHING)

class Members(models.Model):
    user = models.ForeignKey(Users,on_delete = models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete = models.DO_NOTHING)
    rol = models.CharField(max_length=60)
    date = models.DateTimeField()