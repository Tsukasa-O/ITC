from django.db import models
from utils.random_string import random_string_generator
from django.contrib.auth import get_user, get_user_model
from django.utils import timezone

User = get_user_model()

from django.db.models import Q #インポート

def slug_maker():
    repeat = True
    while repeat:
        new_slug = random_string_generator()
        counter = NippoModel.objects.filter(slug=new_slug).count()
        if counter == 0:
            repeat = False
    return new_slug

class NippoModelQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        qs = qs.filter(public=True)
        if query is not None:
            or_lookup = (
                Q(title__icontains=query)|
                Q(content__icontains=query)            
            )
            qs = qs.filter(or_lookup).distinct()
        return qs.order_by("-date")
    
class NippoModelManager(models.Manager):
    def get_queryset(self):
        return NippoModelQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class NippoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="タイトル")
    content = models.TextField(max_length=1000, verbose_name="内容")
    public = models.BooleanField(default=False, verbose_name="公開する")
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=20, unique=True, default=slug_maker)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "日報"
        verbose_name_plural = "日報一覧"
        
    objects = NippoModelManager()

    
    def __str__(self):
        return self.title
    
    def get_profile_page_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy("nippo-list") + f"?profile={self.user.profile.id}"