from django import forms
from . models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','released_year','actors']
        labels={
            'title':'Enter Movie Title',
            'released_year':'Select Released_year',
            'Actors':'Select Actors'
        }
        widgets={
            'title':forms.TextInput(attrs={'placeholder':'Enter movie name..'}),
            'released_year':forms.DateInput(attrs={'type':'date'}),
            'actors':forms.CheckboxSelectMultiple()   
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        common_class="form-control"

        for field in self.fields.values():
            field.widget.attrs.update({'class':common_class})