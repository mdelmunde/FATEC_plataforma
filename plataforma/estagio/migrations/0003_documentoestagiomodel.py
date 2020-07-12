# Generated by Django 2.2.13 on 2020-07-08 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estagio', '0002_auto_20200625_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoEstagioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.TextField(default='')),
                ('tipo_documento', models.CharField(choices=[('1', 'Termo de compromisso de Estágio'), ('2', 'Plano de Atividades'), ('3', 'Termo Aditivo'), ('4', 'Rescisão de Contrato'), ('5', 'Ficha de avaliação do estagiário'), ('6', 'Relatório Parcial de Estágio'), ('7', 'Relatório Final de Estágio')], default='1', max_length=2, verbose_name='Tipo de Documento')),
                ('curso_fatec', models.CharField(choices=[('1', 'Sistemas para Internet'), ('2', 'Gestão Empresarial')], default='1', max_length=2, verbose_name='Curso')),
                ('documento', models.FileField(upload_to='documentos_estagio/')),
                ('observacao', models.TextField(blank=True, default='')),
                ('observacao_professor', models.TextField(blank=True, default='')),
                ('aprovado_professor', models.BooleanField(default=False)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Documento de Estágio',
                'verbose_name_plural': 'Documentos de Estágio',
            },
        ),
    ]
