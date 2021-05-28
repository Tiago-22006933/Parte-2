from . import views
from django.urls import path, include

app_name = "lmdb"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('streaming/', views.streaming_page_view, name='streaming'),
    path('filmes/', views.filmes_page_view, name='filmes'),
    path('contacto/', views.contacto_page_view, name='contacto'),
    path('ajax/validate_username/', views.contacto_page_view),
    path('comentarios/', views.comentarios_page_view, name='comentarios'),
]