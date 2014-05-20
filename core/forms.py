from django import forms


class IssueForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField(required=False, widget=forms.Textarea)
