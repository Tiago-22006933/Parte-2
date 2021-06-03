from . import views
from django.urls import path, include

app_name = "lmdb"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('streaming/', views.streaming_page_view, name='streaming'),
    path('pesquisa/', views.pesquisa_page_view, name='pesquisa'),
    path('contacto/', views.contacto_page_view, name='contacto'),
    path('ajax/validate_username/', views.contacto_page_view),
    path('comentarios/', views.comentarios_page_view, name='comentarios'),
    path('', views.index_view, name="index"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]