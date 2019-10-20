from django import forms

from .models import *

class PlayDetailForm(forms.ModelForm):

    class Meta:
        model = PlayDetail
        fields = ['player1','player2']

