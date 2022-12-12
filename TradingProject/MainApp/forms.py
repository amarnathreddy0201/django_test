from django import forms
class EventsForm(forms.Form):
    time=forms.TimeField()
    date=forms.DateField()