from django.shortcuts import render
from posts.models import GhostPost
from posts.forms import AddForm



# Create your views here.
def index(req):
    posts = Ghostpost.objects.all()
    form = AddForm()
    if request.method == "POST":
        form = AddForm(req.POST)
        form.save()
    return render(req, 'index.html', {'posts': posts})

