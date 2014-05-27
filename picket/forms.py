from django import forms

from .documents import Project


class IssueForm(forms.Form):

    project = forms.ModelChoiceField(queryset=Project.objects.all())
    subject = forms.CharField()
    text = forms.CharField(required=False, widget=forms.Textarea)


class ProjectForm(forms.Form):

    name = forms.CharField()
