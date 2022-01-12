import django_tables2 as tables
from .models import things

class SomeTable(tables.Table):

    class Meta:
        model= things
        attrs = {"class": "paleblue"}