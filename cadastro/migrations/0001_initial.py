# Generated by Django 4.0.4 on 2022-05-15 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id_cidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cidade', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cidades',
                'db_table': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id_conta', models.AutoField(primary_key=True, serialize=False)),
                ('tp_conta', models.CharField(choices=[('poupança', 'poupança'), ('corrente', 'corrente')], default='poupança', max_length=30)),
                ('id_banco', models.IntegerField()),
                ('banco', models.CharField(choices=[('banco 1', 'banco 1'), ('banco 2', 'banco 2'), ('banco 3', 'banco 3'), ('banco 4', 'banco 4')], default='banco 1', max_length=50)),
                ('conta', models.IntegerField()),
                ('agencia', models.IntegerField()),
                ('operacao', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Contas',
                'db_table': 'Contas',
            },
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id_enderecos', models.AutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=8)),
                ('cep', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=80)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('id_cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.cidades')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
                'db_table': 'Enderecos',
            },
        ),
        migrations.CreateModel(
            name='Ufs',
            fields=[
                ('id_uf', models.AutoField(primary_key=True, serialize=False)),
                ('nome_uf', models.CharField(max_length=30)),
                ('sigla_uf', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Ufs',
                'db_table': 'Ufs',
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('vinculo', models.CharField(choices=[('vinculo 1', 'vinculo 1'), ('vinculo 2', 'vinculo 2')], default='vinculo 1', max_length=20)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.IntegerField(max_length=11)),
                ('id_conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.contas')),
                ('id_endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.enderecos')),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'db_table': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencias',
            fields=[
                ('id_ocorrencia', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('realizada', models.BooleanField(default=True)),
                ('ocorrencia', models.TextField(max_length=100000)),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.pessoas')),
            ],
            options={
                'verbose_name_plural': 'Ocorrências',
                'db_table': 'Ocorrencias',
            },
        ),
        migrations.AddField(
            model_name='cidades',
            name='id_uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.ufs'),
        ),
    ]
