from django.db import models

# Create your models here.
class IngredientCategory(models.Model):
    name = models.CharField(max_length = 256, blank = False, null = False)
    description = models.TextField(max_length = 500, default = "", blank = True, null = True)

    def __str__(self):
        return (self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length = 256, blank = False, null = False)
    categories = models.ForeignKey(IngredientCategory, null=True, blank = True, on_delete=models.SET_NULL)
    description = models.TextField(max_length = 500, default = "", blank = True, null = True)

    def __str__(self):
        return( self.categories.name + "---" + self.name )
