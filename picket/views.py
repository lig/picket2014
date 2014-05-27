from actionviews import ActionResponse, TemplateView
from actionviews.decorators import action_decorator, child_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from mongoengine.django.shortcuts import get_document_or_404

from .documents import Issue, Project
from .forms import IssueForm, ProjectForm


class IssueView(TemplateView):

    def get_queryset(self):
        qs = Issue.objects.all()
        project=self.context.get('project')

        if project:
            qs = qs.filter(project=project)

        return qs

    def do_list(self:'', page:r'\d+'=1):
        issues = self.get_queryset()
        return {'issues': issues}

    @action_decorator(login_required)
    def do_create(self):
        request = self.request

        if request.method == 'POST':
            form = IssueForm(request.POST)

            if form.is_valid():
                issue = Issue(
                    project=form.cleaned_data['project'],
                    subject=form.cleaned_data['subject'],
                    creator=request.user,
                    comments=[form.cleaned_data['text']])
                issue.save()
                context_project = self.context.get('project')
                return (context_project and
                    redirect('list', context_project.id) or
                    redirect('list'))

        else:
            form = IssueForm(initial={'project': self.context.get('project')})

        return {'form': form}

    def do_issue(self, n:r'\d+'):
        return {'issue': get_document_or_404(Issue, id=int(n))}


class ProjectView(TemplateView):

    @child_view(IssueView)
    def do_project(self:'', project):
        return {'project': get_document_or_404(Project, pk=project)}

    @action_decorator(login_required)
    def do_project_create(self):
        # @todo: allow this method to be called `do_create`
        request = self.request

        if request.method == 'POST':
            form = ProjectForm(request.POST)

            if form.is_valid():
                project = Project(**form.cleaned_data)
                project.save()
                return redirect('list', project=project.id)

        else:
            form = ProjectForm()

        return {'form': form}
