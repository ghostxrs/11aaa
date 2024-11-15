from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import News, Category, Region
# Create your views here.
def home(request):
    first_news = News.objects.first()
    three_news = News.objects.all()[1:4]
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news,
    })
def all_news(request):
    all_news = News.objects.all()
    return render(request, 'all-news.html', {
        'all_news': all_news
    })
def detail(request, id):
    news = News.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    context = {'news': news,
               'category': category,
               'rel_news': rel_news}
    return render(request, 'detail.html', context)
def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats
    })
def category(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': category
    })

def all_region(request):
    regs = Region.objects.all()
    return render(request, 'region.html', {
        'regs': regs
    })
def region(request, pk):
    region = Region.objects.get(id=pk)
    regs = News.objects.filter(region=region)
    return render(request, 'region-news.html', {
        'all_regs' :regs,
        'region':region
    })
class Create_post(CreateView):
    model = News
    template_name = 'create-post.html'
    fields = ['category', 'region', 'title', 'body', 'image', 'author']
class Edit_post(UpdateView):
    model = News
    template_name = 'edit-post.html'
    fields = ['category', 'region', 'title', 'body']
class Delete_post(DeleteView):
    model = News
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')