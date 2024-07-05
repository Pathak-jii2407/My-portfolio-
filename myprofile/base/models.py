from django.db import models

from django.db import models

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    project_file = models.FileField(upload_to='projects/')
    project_name = models.CharField(max_length=100)  

    def __str__(self):
        return self.project_name

class Survey(models.Model):
    RATING_CHOICES = [
        (1, '1 - cry'),
        (2, '2 - serious'),
        (3, '3 - happy'),

    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField()

