import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.db.models import Avg
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import NovoContactoForm, NovoComentarioForm, NovoRealizadorForm, NovoActorForm, NovoFilmeForm
from .models import Contacto, Comentario, Streaming, Genero, Realizador, Actor, Filme

def home_page_view(request):
	return render(request, 'lmdb/home.html')

def streaming_page_view(request):
	context = {'streaming_plat': Streaming.objects.all()}
	return render(request, 'lmdb/streaming.html', context)

def filmes_page_view(request):
	filmes = Filme.objects.all()
	context = {'filmes': filmes}
	return render(request, 'lmdb/filmes.html', context)

def novo_filme_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('lmdb:login'))
	form_realizador = NovoRealizadorForm(request.POST or None, prefix='realizador_form')
	form_actor = NovoActorForm(request.POST or None, prefix='actor_form')
	form_filme = NovoFilmeForm(request.POST or None, request.FILES, prefix='filme_form')

	generos = Genero.objects.all()
	realizadores = Realizador.objects.all()
	actores = Actor.objects.all()

	if form_realizador.is_valid() and form_realizador.prefix == 'realizador_form':
		form_realizador.save()
		return HttpResponseRedirect(reverse('lmdb:novofilme'))

	if form_actor.is_valid() and form_actor.prefix == 'actor_form':
		form_actor.save()
		return HttpResponseRedirect(reverse('lmdb:novofilme'))

	if form_filme.is_valid() and form_filme.prefix == 'filme_form':
		form_filme.save()
		return HttpResponseRedirect(reverse('lmdb:novofilme'))

	print(form_filme.errors)
	context = {
		'generos': generos,
		'realizadores': realizadores,
		'actores': actores,
		'form_realizador': form_realizador,
		'form_actor': form_actor,
		'form_filme': form_filme,
	}
	return render(request, 'lmdb/novofilme.html', context)

def contacto_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('lmdb:login'))
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
		Contacto.objects.filter(pk=editar_id).update(telefone=request.POST.get('telefone'))
		Contacto.objects.filter(pk=editar_id).update(data_nascimento=request.POST.get('data_nascimento'))
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
	num_comentários = Comentario.objects.all().count()
	avg_clareza = Comentario.objects.all().aggregate(Avg('clareza'))
	avg_rigor = Comentario.objects.all().aggregate(Avg('rigor'))
	avg_precisão = Comentario.objects.all().aggregate(Avg('precisão'))
	avg_profundidade = Comentario.objects.all().aggregate(Avg('profundidade'))
	avg_amplitude = Comentario.objects.all().aggregate(Avg('amplitude'))
	avg_lógica = Comentario.objects.all().aggregate(Avg('lógica'))
	avg_significância = Comentario.objects.all().aggregate(Avg('significância'))
	avg_originalidade = Comentario.objects.all().aggregate(Avg('originalidade'))
	avg_globalidade = Comentario.objects.all().aggregate(Avg('globalidade'))

	form = NovoComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('lmdb:comentarios'))

	context = {
		'form': form,
		'clareza': avg_clareza,
		'rigor': avg_rigor,
		'precisão': avg_precisão,
		'profundidade': avg_profundidade,
		'amplitude': avg_amplitude,
		'lógica': avg_lógica,
		'significância': avg_significância,
		'originalidade': avg_originalidade,
		'globalidade': avg_globalidade,
		'num_comentários': num_comentários,
	}
	print(context)
	return render(request, 'lmdb/comentarios.html', context)

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('lmdb:home'))
		else:
			return render(request, "lmdb/login.html", {
				'message': "Credenciais incorrectas."
			})
	return render(request, "lmdb/login.html")

def logout_view(request):
	logout(request)
	return render(request, 'lmdb/home.html')