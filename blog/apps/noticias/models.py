from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    resumen = models.TextField
    contenido= models.TextField
    fecha_de_publicacion= models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete=(models.CASCADE))

    def __str__(self):
        return self.titulo
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    resumen = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    #para imagen debemos instalar pillow
    imagen = models.ImageField(upload_to= 'noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.CASCADE) #SET_NULL
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk) 
# se agregó el campo author que hace referencia al autor de la noticia, el “default=Usuario.objects.get(is_superuser=True).pk” esta ahi para que tome por defecto (de las noticias que ya tenía creadas) como usuario al superusuario, otra manera de hacerlo es admitiendo valores nulos con “default=null”         
    def __str__(self):
        return self.titulo