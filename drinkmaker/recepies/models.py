from django.db import models
from rawingredients.models import Ingredient

class MeasurementSize(models.Model):
    name = models.CharField(max_length = 256, blank = False, null = False)
    unit = models.CharField(max_length = 10, blank = True, null = True)
    description = models.TextField(max_length = 500, default = "", blank = True, null = True)
    def __str__(self):
        if self.unit is None or self.unit is "":
            return(self.name)
        else:
            return(self.unit)

# Create your models here.
class Recepie(models.Model):
    name = models.CharField(max_length = 256, blank = False, null = False)
    ingredients = models.ManyToManyField(Ingredient, through = "IngredientList", through_fields= ('recepie', 'ingredient'))
    description = models.TextField(max_length = 500, default = "", blank = True, null = True)

    post_drink_instruction = models.TextField(max_length = 500, blank = True, null = True) #save what to do after poring, drink, or what garnish to add, etc


    #Ratings for this recepie
    number_of_ratings_global = models.IntegerField(default = 0)
    average_rating_global = models.IntegerField(default = 0) #this is the number of starts out of 10
    number_of_ratings_local = models.IntegerField(default = 0)
    average_rating_local = models.IntegerField(default = 0)

    #number of times consumed
    number_of_times_consumed_local = models.IntegerField(default = 0)
    number_of_times_consumed_global = models.IntegerField(default = 0)

    comments = models.CharField(max_length = 256, blank = True, null = True, default = "No Comments") #local comments for the user, this comment will be added to the server as a cumulative comment


class IngredientList(models.Model):
    recepie = models.ForeignKey(Recepie, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits = 8, decimal_places=3)
    quantity_size = models.ForeignKey(MeasurementSize)
