from django.shortcuts import render,redirect
from .models import Sala
from .forms import SalaForm
from .models import Material
from .forms import MaterialForm


# Create your views here.
def inicio (request):
	return render(request,'app/inicio.html')

def listar_salas(request):
	sls = Sala.objects.all()
	return render(request, 'app/sala/listar_salas.html', {'salas': sls})

def cadastrar_salas(request):
	if(request.method == "POST"):
		form = SalaForm(request.POST)
		if form.is_valid():
			sala = form.save(commit=False)
			sala.save()
			return redirect('/listar_salas')

	else:
		form = SalaForm()
		return render(request,'app/sala/cadastrar_salas.html',{'form': form})

def listar_materiais(request):
	mtr = Material.objects.all()
	return render(request, 'app/material/listar_material.html',{'material': mtr})

def cadastrar_materiais(request):
	if(request.method == "POST"):
		form = MaterialForm(request.POST)
		if form.is_valid():
			material = form.save(commit=False)
			material.save()
			return redirect('/listar_materiais')

	else:
		form = MaterialForm()
		return render(request,'app/material/cadastrar_material.html', {'form': form})
		