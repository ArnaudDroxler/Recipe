from django.contrib import admin


from .models import *

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Unit)
admin.site.register(Instruction)
admin.site.register(Ingredient)