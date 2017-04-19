from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from rawingredients.models import Ingredient
# Create your models here.
class MachineSettings(models.Model):
    name = models.CharField(max_length = 256, blank = False, null = False)
    description = models.TextField(max_length = 500, default = "", blank = True, null = True)

#this will have information for channels 1 through 4
class Channel(models.Model):
    channel_number = models.IntegerField(unique = True,
                validators=[    MaxValueValidator(4),
                                MinValueValidator(1)] )
    name = models.CharField(max_length = 256, default = "Channel",blank = False, null = False)
    active = models.BooleanField(default = False)

#each tap belongs to one of the 4 channels
class Tap(models.Model):
    channel = models.ForeignKey(Channel)
    tap_number = models.IntegerField( validators=[ MaxValueValidator(8), MinValueValidator(1)] )
    name = models.CharField(max_length = 256, default = "Channel",blank = False, null = False)
    ingredient = models.ForeignKey(Ingredient)

    class Meta:
        unique_together = ('channel','tap_number')
