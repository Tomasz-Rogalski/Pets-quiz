from .models import Game

from django import forms

class GameForm(forms.ModelForm):
  class Meta:
    model = Game
    fields = ['player_name', 'category', 'pet']
    widgets =  {
            'player_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.RadioSelect(attrs={'class': 'd-inline'}),
            'pet': forms.RadioSelect(attrs={'class': 'd-inline'}),
            }
