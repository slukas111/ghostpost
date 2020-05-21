from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.models import GhostPost
from posts.forms import AddForm
from datetime import datetime



def index(req):
    posts = GhostPost.objects.all().order_by('-time_post')
    form = AddForm()
    if req.method == "POST":
        form = AddForm(req.POST)
        if form.is_valid():
            posts = form.cleaned_data
        form.save()
        return HttpResponseRedirect(reverse("home"))
    return render(req, 'index.html',{'form':form,'posts':posts})



def post_view(req, id):
    data = GhostPost.objects.get(id=id)
    return render(req, 'html', {'post': post})

# def total_view():

# def boast_view():

# def upvote_view():

# def downvote_view():



