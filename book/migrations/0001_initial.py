# Generated by Django 4.0.4 on 2022-04-30 12:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('I', 'I BOB. SMM – IJTIMOIY MEDIA MARKETING'), ('II', 'II BOB. SMM LOYIHALARI BILAN ISHLASH'), ('III', 'III BOB. CMS – KONTENT BOSHQARUV TIZIMLARI'), ('IV', 'IV BOB. LMS – TA’LIMNI BOSHQARUV TIZIMLARI'), ('V', 'V BOB. MOOC – OMMAVIY OCHIQ ONLAYN KURSLAR'), ('VI', 'VI BOB. WEB-FREELANCE – INTERNET ORQALI DAROMAD OLISH')], max_length=5)),
                ('title', models.CharField(max_length=512, verbose_name='Mavzu')),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Mavzu',
                'verbose_name_plural': 'Mavzular',
            },
        ),
    ]
