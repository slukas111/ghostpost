from django.db import models
from django.utils import timezone

# Create your models here.
# [x]One model to represent both boasts and roasts
# [x]Boolean to tell whether it's a boast or a roast
# [x]CharField to put the content of the post in
# [x]IntegerField for up votes
# [x]IntegerField for down votes
# [x]DateTimeField for submission time

class GhostPost(models.Model):
    total_both = models.IntegerField(default=0)
    is_boast = models.BooleanField()
    post = models.CharField(max_length=500)
    up_votes= models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    time_post =models.DateTimeField(default=timezone.now)

