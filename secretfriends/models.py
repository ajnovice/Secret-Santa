from django.db import models

# Create your models here.
class unique_list(models.Model):
    sha = models.CharField(max_length=1000)
    unique_sha = models.CharField(max_length=1000)
    
    def __unicode__(self):
	return (self.sha)