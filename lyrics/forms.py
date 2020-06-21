from django import forms

class Song(forms.ModelForm):
    artist = forms.CharField()
    song = forms.CharField()