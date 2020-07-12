import hashlib
import random
from django import forms
from django.forms import ModelForm
from estagio.models import ConvenioModel, DocumentoEstagioModel


class ConvenioForm(ModelForm):
    class Meta:
        model = ConvenioModel
        fields = ('empresa', 'documento', 'observacao')
        labels = {
            'documento': 'Arquivo',
            'observacao': 'Observação',
        }
        widgets = {
            'empresa': forms.HiddenInput(),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'empresa': {
                'required': ("Informe ID da empresa."),
            },
            'documento': {
                'required': ("Informe um arquivo."),
            }
        }

    def renomear_arquivo(self, nome):
        sufixo = nome[-5:]
        nome = hashlib.sha256(
            str(random.getrandbits(256)).encode('utf-8')).hexdigest()
        nome = nome + sufixo
        return nome

    def clean_observacao(self):
        return self.cleaned_data['observacao'].upper()


class DocumentoEstagioForm(ModelForm):
    class Meta:
        model = DocumentoEstagioModel
        fields = ('empresa', 'tipo_documento', 'curso_fatec', 'nome_aluno',
                  'documento', 'observacao')
        labels = {
            'documento': 'Arquivo',
            'tipo_documento':'Tipo de Documento',
            'curso_fatec': 'Curso',
            'nome_aluno': 'Nome do Aluno',
            'observacao': 'Observação',
        }
        widgets = {
            'empresa': forms.HiddenInput(),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'curso_fatec': forms.Select(attrs={'class': 'form-control'}),
            'nome_aluno': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'documento': {
                'required': ("Informe um arquivo."),
            }
        }

    def renomear_arquivo(self, nome):
        sufixo = nome[-5:]
        nome = hashlib.sha256(
            str(random.getrandbits(256)).encode('utf-8')).hexdigest()
        nome = nome + sufixo
        return nome

    def clean_observacao(self):
        return self.cleaned_data['observacao'].upper()

    def clean_nome_aluno(self):
        return self.cleaned_data['nome_aluno'].upper()

