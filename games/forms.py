from django import forms

class PlayerForm(forms.Form):
    player_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search players'}))
