from django.shortcuts import render
from posts.models import GhostPost
from posts.forms import AddForm


# Create your views here.
def index(req):
    posts = GhostPost.objects.all()
    form = AddForm()
    if req.method == "POST":
        form = AddForm(req.POST)
        form.save()
    return render(req, 'index.html', {'posts': posts})

