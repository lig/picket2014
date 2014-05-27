from django import forms

from .documents import Project


class ProjectForm(forms.Form):

    name = forms.CharField()


class IssueForm(forms.Form):

    project = forms.ModelChoiceField(queryset=Project.objects.all())
    subject = forms.CharField()
    text = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.Form):

    text = forms.CharField(required=False, widget=forms.Textarea)
