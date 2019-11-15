from django import forms

from .models import *

class PlayDetailForm(forms.ModelForm):

    class Meta:
        model = PlayDetail
        fields = ['player1','player2']

    def __init__(self, *args, **kwargs):
        super(PlayDetailForm, self).__init__(*args, **kwargs)
        self.fields['player1'].label = "P1"
        self.fields['player2'].label = "P2"