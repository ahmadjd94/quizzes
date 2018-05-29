from django import forms


class FeedbackForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea, max_length=500)
