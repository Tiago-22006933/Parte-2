import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import NovoContactoForm, NovoComentarioForm
from .models import Contacto, Comentario, Streaming

def home_page_view(request):
	return render(request, 'lmdb/home.html')

def streaming_page_view(request):
	context = {'streaming_plat': Streaming.objects.all()}
	print(Streaming.objects.all())
	return render(request, 'lmdb/streaming.html', context)

def filmes_page_view(request):
	return render(request, 'lmdb/filmes.html')

def contacto_page_view(request):
	form = NovoContactoForm(request.POST or None)
	if 'edita_contacto_id' in request.POST.keys():
		editar_id = request.POST.get('edita_contacto_id')
		contacto_a_editar = Contacto.objects.get(pk=editar_id)
		json_data = serializers.serialize("json", [contacto_a_editar])
		return HttpResponse(json_data, content_type="application/json")
	if 'edita_contacto_flag' in request.POST.keys():
		editar_id = request.POST.get('edita_contacto_id1')
		Contacto.objects.filter(pk=editar_id).update(first_name = request.POST.get('first_name'))
		Contacto.objects.filter(pk=editar_id).update(last_name = request.POST.get('last_name'))
		Contacto.objects.filter(pk=editar_id).update(email = request.POST.get('email'))
		return HttpResponseRedirect(reverse('lmdb:contacto'))
	if 'contacto_id' in request.POST.keys():
		contacto_eliminar = request.POST.get('contacto_id')
		Contacto.objects.get(pk=contacto_eliminar).delete()
		return HttpResponseRedirect(reverse('lmdb:contacto'))
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('lmdb:contacto'))

	context = {'contactos': Contacto.objects.all(), 'form': form}
	return render(request, 'lmdb/contacto.html', context)

def comentarios_page_view(request):
	form = NovoComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('lmdb:comentarios'))

	context = {'form': form}
	return render(request, 'lmdb/comentarios.html', context)

def index_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('login'))
	return render(request, "lmdb/user.html")

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, "lmdb/login.html", {
				'message': "Invalid credentials."
			})
	return render(request, "lmdb/login.html")

def logout_view(request):
	logout(request)
	return render(request, 'lmdb/login.html', {
		"message: Logged out."
	})