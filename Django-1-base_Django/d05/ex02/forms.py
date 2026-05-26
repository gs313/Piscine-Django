from django import forms

class HistoryForm(forms.Form):
    text_input = forms.CharField(label='Enter text', max_length=200)
