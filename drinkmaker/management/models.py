from django.db import models

# Create your models here.
class DefaultUserSettings(models.Model):
    name = models.CharField(max_length = 256, null = False, blank = False)
    email_address = models.EmailField(null = True, blank = True)
    pin = models.CharField(max_length = 6, null=True, blank = True)
    initial_setup_complete = models.BooleanField(default = False)
