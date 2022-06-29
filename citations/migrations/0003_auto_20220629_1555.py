# Generated by Django 3.2.12 on 2022-06-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citations', '0002_alter_citation_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='citation',
            name='issn',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='ISSN'),
        ),
        migrations.AddField(
            model_name='citation',
            name='issn_size_set',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='ISSN size set'),
        ),
        migrations.AddField(
            model_name='citation',
            name='standardization_key',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Standardization key'),
        ),
        migrations.AddField(
            model_name='citation',
            name='standardization_method',
            field=models.CharField(blank=True, choices=[('0', "Associação exata do título com base 'ISSN-Attrs'"), ('1', "Associação exata do título com mais de um código ISSN e desambiguação com base 'ISSN-Year-Volume'"), ('2', "Associação exata do título com mais de um código ISSN e desambiguação com base 'ISSN-Year-Volume' e volume inferido"), ('3', "Associação exata do título com mais de um código ISSN e desambiguação com base 'ISSN-Year-Volume-Artifitial'"), ('4', "Associação exata do título com mais de um código ISSN e desambiguação com base 'ISSN-Year-Volume-Artifitial' e volume inferido"), ('11', "Associação aproximada do título com um ou mais códigos ISSN e desambiguação com base 'ISSN-Year-Volume'"), ('12', "Associação aproximada do título com um ou mais códigos ISSN e desambiguação com base 'ISSN-Year-Volume' e volume inferido"), ('13', "Associação aproximada do título com um ou mais códigos ISSN e desambiguação com base 'ISSN-Year-Volume-Artifitial'"), ('14', "Associação aproximada do título com um ou mais códigos ISSN e desambiguação com base 'ISSN-Year-Volume-Artifitial' e volume inferido"), ('519', "Associação exata do título com mais de um código ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume'"), ('529', "Associação exata do título com mais de um código ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume' e volume inferido"), ('539', "Associação exata do título com mais de um código ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume-Artifitial'"), ('549', "Associação exata do título com mais de um código ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume-Artifitial' e volume inferido"), ('619', "Associação aproximada do título com um ou mais códigos ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume'"), ('629', "Associação aproximada do título com um ou mais códigos ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume' e volume inferido"), ('639', "Associação aproximada do título com um ou mais códigos ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume-Artifitial'"), ('649', "Associação aproximada do título com um ou mais códigos ISSN, mas sem desambiguação possível com base 'ISSN-Year-Volume-Artifitial' e volume inferido"), ('500', 'Associação exata do título com mais de um códigos ISSN, mas nenhuma base foi capaz de decidir qual é o correto'), ('600', 'Associação aproximada do título com um ou mais códigos ISSN, mas nenhuma base foi capaz de decidir qual é o correto'), ('70', "Título não foi encontrado na base 'ISSN-Attrs"), ('80', 'Associação exata do título com mais de um código ISSN, mas não foi possível decidir qual é o correto, pois o ano informado é inválido'), ('81', 'Associação aproximada do título com mais de um código ISSN, mas não foi possível decidir qual é o correto, pois o ano informado é inválido'), ('82', 'O título não foi informado'), ('90', 'Não foi realizada tentativa de associar o título a um código ISSN, pois existe código DOI'), ('91', 'Não foi realizada tentativa de associar o título a um código ISSN de modo aproximado devido à indicação do usuário')], max_length=3, null=True, verbose_name='Standardization method'),
        ),
        migrations.AlterField(
            model_name='citation',
            name='citation_code',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Citation code'),
        ),
    ]