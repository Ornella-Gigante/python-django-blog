from django.shortcuts import render
from .models import Post
# Create your views here.

""" 
Aqui se definirán funciones para que se renderice al buscar en la raíz del sitio 

"""


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts":posts}) #haciendo remferencia a la app y la plantilla


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {"post":post})
