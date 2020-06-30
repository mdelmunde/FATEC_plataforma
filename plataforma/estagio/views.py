from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse as r
from core.facade import area_student, area_teacher, area_company
from estagio.forms import ConvenioForm
from estagio.models import ConvenioModel
from plataforma import settings


@area_teacher
def listar_todos_convenios(request):
    context = {'media_url': settings.MEDIA_URL,
               'convenios': ConvenioModel.objects.all()}
    return render(request, 'validar_convenio.html', context)


@area_teacher
def validar_convenio(request):
    if request.method == 'GET':
        context = {'media_url': settings.MEDIA_URL,
                'convenios': ConvenioModel.objects.all()}
        return render(request, 'validar_convenio.html', context)
    else:
        pass

@area_company
def upload_convenio(request):
    if request.method == 'GET':
        context = {'form': ConvenioForm(
            initial={"empresa": request.user.pk})}
        return render(request, 'upload_convenio.html', context)
    else:
        form = ConvenioForm(request.POST, request.FILES)
        if form.is_valid():
            novo_nome = form.renomear_arquivo(form.files['documento'].name)
            form.files['documento'].name = novo_nome
            ConvenioModel.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(r('core:core_index_empresa'))
        else:
            context = {'form': form}
            return render(request, 'upload_convenio.html', context)


@area_company
def convenio_por_empresa(request):
    if request.method == 'GET':
        context = {'media_url': settings.MEDIA_URL,
                   'convenios': ConvenioModel.objects.all()}
        return render(request, 'convenio_por_empresa.html', context)