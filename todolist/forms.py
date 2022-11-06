from django.forms import ModelForm
from .models import Item_todolist

class formtodo(ModelForm):
    class Meta:
        model = Item_todolist
        fields = ['date','title','description']