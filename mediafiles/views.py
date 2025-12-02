from django.shortcuts import render
from .models import Image

def gallery_view(request):
    files = Image.objects.all()
    return render(request, "mediafiles/list.html", {"files": files})
