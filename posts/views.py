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
            form.save()
        return HttpResponseRedirect(reverse("homepage"))
    return render(req, 'index.html',{'form':form,'posts':posts})


def post_view(req, id):
    data = GhostPost.objects.get(id=id)
    return render(req, 'post_view.html', {'data': data})


def boast_view(request):
    data = GhostPost.objects.filter(is_boast=True).order_by('-time_post')
    return render(request, 'index.html', {'posts':data})

def roast_view(request):
    data= GhostPost.objects.filter(is_boast=False).order_by('-time_post')
    return render(request, 'index.html', {'posts':data})

def vote_view(request):
    data = GhostPost.objects.order_by('-total_both')
    return render(request, 'index.html', {'posts':data})

def up_vote(request, post_id):
    post = GhostPost.objects.get(id=post_id)
    post.total_both +=1
    post.save()
    return HttpResponseRedirect(reverse('post_view', kwargs={'id': post_id}))

def down_vote(request, post_id):
    post = GhostPost.objects.get(id = post_id)
    post.total_both -= 1
    post.save()
    return HttpResponseRedirect(reverse('post_view', kwargs={'id': post_id}))



