from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=250, default="", null=False)

    def __str__(self):
        return self.tag

class Recipe(models.Model):
    name = models.CharField(max_length=100, null=False)
    duration = models.IntegerField(default=0, null=False)
    serving = models.IntegerField(default=1, null=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "Id :" + str(self.pk) + " Name :" + self.name

class Unit(models.Model):
    name = models.CharField(max_length=25, default="", null=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, default="", null=False)
    amount = models.FloatField(default=1, null=False)
    unit = models.OneToOneField(Unit, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + " " + self.name


class Instruction(models.Model):
    text = models.TextField(max_length=10000, default="", null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    sort = models.IntegerField()

    def __str__(self):
        return str(self.pk)