from .documents import Project


def projects(request):
    return {'projects': Project.objects.all()}
