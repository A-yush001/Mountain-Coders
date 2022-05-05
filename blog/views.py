from django.forms import SlugField
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog,Contact

def home(request):
    return render(request,'index.html')


def blog(request):
    no_of_posts=3
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
    print(page)
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return  render(request,'bloghome.html',context)


def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={"blog":blog}
    return render(request,'blogpost.html',context)


def search(request):
    return  render(request,'search.html')


def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
    return  render(request,'contact.html')
