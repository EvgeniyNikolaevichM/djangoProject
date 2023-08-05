# Generated by Django 4.0 on 2022-06-02 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='law_for_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('law_type_plat', models.CharField(max_length=50, verbose_name='Наименование типа закона')),
                ('amplitude', models.IntegerField(verbose_name='Амплитуда закона от 0 до 100')),
                ('coordinates_t', models.JSONField(verbose_name='Координаты и параметры для платформы')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='law_for_platform_wave_user_created', to='auth.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Закон движения для базового модуля',
                'verbose_name_plural': 'Законы движения для базового модуля',
            },
        ),
        migrations.CreateModel(
            name='system_stewart_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_system', models.CharField(max_length=50, verbose_name='Наименование системы')),
                ('discription_system', models.CharField(max_length=500, verbose_name='Описание системы')),
                ('law_type_system', models.CharField(blank=True, choices=[('Волна', 'Волна'), ('Колебания', 'Колебания')], default='Волна', help_text='Выбрать из списка', max_length=50, verbose_name='Закон движения системы')),
                ('x_max_matrix', models.IntegerField(verbose_name='Размер матрицы по оси x')),
                ('y_max_matrix', models.IntegerField(verbose_name='Размер матрицы по оси y')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='system_stewart_platform_user_created', to='auth.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Система Stewart Platform',
                'verbose_name_plural': 'Системы Stewart Platform',
            },
        ),
        migrations.CreateModel(
            name='stewart_platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_platform', models.CharField(max_length=50, verbose_name='Наименование базового модуля')),
                ('discription_platform', models.CharField(max_length=500, verbose_name='Описание базового модуля')),
                ('ip_adress', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('port_platform', models.PositiveSmallIntegerField(default=0, verbose_name='Порт подключения')),
                ('position_x_in_matrix', models.IntegerField(verbose_name='Позиция базового модуля в матрице по оси х')),
                ('position_y_in_matrix', models.IntegerField(verbose_name='Позиция базового модуля в матрице по оси у')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stewart_platform_user_created', to='auth.user', verbose_name='Пользователь')),
                ('law_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.law_for_platform', verbose_name='Закон движения платформы')),
                ('system_stewart_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemStewartPlatform.system_stewart_platform', verbose_name='Система')),
            ],
            options={
                'verbose_name': 'Базовый модуль',
                'verbose_name_plural': 'Базовые модули',
            },
        ),
    ]