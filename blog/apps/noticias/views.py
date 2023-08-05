from django.shortcuts import render,redirect
from .models import Noticia,Categoria
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm
from django.urls import reverse
# Create your views here.
@login_required
def ListarNoticias(request):
    contexto = {} #diccionario
    id_categoria = request.GET.get("id", None)


    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() #SELECT * FROM Noticias / lista objetos


    contexto['noticias'] = n


    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['categorias'] = cat


    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticias(request,pk):
    contexto ={}
    n= Noticia.objects.get(pk=pk)
    contexto['noticia']=n
    return render(request, 'noticias/detalle.html', contexto)


def AddNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.author = request.user #autor de la noticia
            noticia.save()
            return redirect('home')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/addNoticia.html', {'form': form})