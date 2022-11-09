from django import forms
from .models import Game


class GameForm(forms.ModelForm):
	'''Form with basic options to start game'''
	class Meta:
		model = Game
		fields = ['player_name', 'category', 'pet']
		widgets =  {
				'player_name' : forms.TextInput(attrs={'class': 'form-control'}),
				'category': forms.RadioSelect(attrs={'class': 'd-inline'}),
				'pet': forms.RadioSelect(attrs={'class': 'd-inline'}),
				}
