from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Post





# Create your views here.
#def home(request):
    #return render(request,'theblog/home.html',{})

class HomeView(ListView):
    model=Post
    template_name='theblog/home.html'
    
class ArticleDetailView(DetailView):
    model=Post
    template_name='theblog/article_details.html'