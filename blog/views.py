# blog/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  # Para mostrar mensajes de error o éxito
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostForm

def index(request):
    return HttpResponse("Hello, World!")

def home(request):
    return render(request, 'blog/home.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        
        # Verificar si el formulario es válido
        if form.is_valid():
            # No es necesario verificar la existencia de un correo electrónico ya que lo eliminamos del modelo
            # Si el formulario es válido, guardar el autor
            form.save()
            
            messages.success(request, "El autor fue creado exitosamente.")
            return redirect('home')  # Redirigir a la página de inicio (o a una lista de autores si lo prefieres)
    else:
        form = AuthorForm()

    # Obtener el nombre del modelo para pasar al template
    model_name = Author._meta.model_name  # Usamos Author aquí directamente

    return render(request, 'blog/create_author.html', {'form': form, 'model_name': model_name})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    model_name = Category._meta.model_name  # Usamos Category aquí directamente
    return render(request, 'blog/create_category.html', {'form': form, 'model_name': model_name})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    model_name = Post._meta.model_name  # Usamos Post aquí directamente
    return render(request, 'blog/create_post.html', {'form': form, 'model_name': model_name})

def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) if query else Post.objects.none()
    return render(request, 'blog/search.html', {'query': query, 'results': results})

# Nueva vista: Acerca de mí
def about(request):
    # Información acerca del dueño de la página
    owner_info = {
        'name': 'Juan Pérez',
        'bio': 'Soy un desarrollador web apasionado por crear aplicaciones fáciles de usar.',
        'contact': 'juanperez@example.com',
        'avatar_url': '/static/images/owner_avatar.jpg',  # Ruta de la imagen del avatar
    }
    
    return render(request, 'blog/about.html', {'owner_info': owner_info})
