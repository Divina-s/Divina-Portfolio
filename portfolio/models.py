from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Experience(models.Model):
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='experience_icons/', blank=True, null=True)  # optional small icon
