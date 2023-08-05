from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




app_name = 'noticias'


urlpatterns = [
    path('', views.ListarNoticias, name='listar'),
    path('listarNoticia/', views.mostrarNoticia.as_view()), #clase
    path('detalle/<int:pk>', views.DetalleNoticias, name='detalle'),
    path('addNoticia', views.AddNoticia, name='addnoticia')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)