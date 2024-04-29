from django import forms 

class PlayerForm(forms.Form):
    player_name = forms.CharField(label='Enter Player Name', max_length=100)