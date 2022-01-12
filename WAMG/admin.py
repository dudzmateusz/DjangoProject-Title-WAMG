from django.forms import *
from django.db.models import *
from .models import *
from django.contrib import admin
from .forms import AddThingsForm

class AddThingsFormAdmin(admin.ModelAdmin):
    form = AddThingsForm

admin.site.register(things, AddThingsFormAdmin)