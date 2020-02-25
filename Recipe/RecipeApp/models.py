from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=250)

    def __str__(self):
        return self.pk

class Recipe(models.Model):
    name = models.CharField(max_length=100, null=False)
    duration = models.IntegerField()
    serving = models.IntegerField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.pk) + " " + self.name

class Unit(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.pk) + " " + self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.OneToOneField(Unit, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + " " + self.name


class Instructions(models.Model):
    text = models.TextField(max_length=10000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    sort = models.IntegerField()

    def __str__(self):
        return self.pk