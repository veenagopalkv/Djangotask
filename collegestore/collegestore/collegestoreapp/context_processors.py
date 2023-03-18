from .models import Department
def menulinks(request):
    links=Department.objects.all()
    return dict(links=links)