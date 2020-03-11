from django.db import models
from autoslug import AutoSlugField

class Tag(models.Model):
    tag = models.CharField(max_length=250, default="", null=False)

    def __str__(self):
        return "Id :" + str(self.pk) + " Tag :" + self.tag

class Recipe(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)
    duration = models.IntegerField(default=0, null=False)
    serving = models.IntegerField(default=1, null=False)
    description = models.TextField(max_length=1000, default="", null=False)
    note = models.TextField(max_length=1000, default="", null=False)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from='name', default="")

    def __str__(self):
        return "Id :" + str(self.pk) + " Name :" + self.name

class Unit(models.Model):
    name = models.CharField(max_length=25, default="", null=False)

    def __str__(self):
        return "Id :" + str(self.pk) + " Unit :" + self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, default="", null=False)
    amount = models.FloatField(default=1, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    unit =  models.ForeignKey(Unit, null=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.pk) + " " + self.name



class Instruction(models.Model):
    text = models.TextField(max_length=10000, default="", null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    sort = models.IntegerField()

    def __str__(self):
        return str(self.pk)