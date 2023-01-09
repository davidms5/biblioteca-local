# Generated by Django 4.1.4 on 2022-12-18 19:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                (
                    "agno_nacimiento",
                    models.DateField(
                        blank=True, null=True, verbose_name="año nacimiento"
                    ),
                ),
                (
                    "fallecimiento",
                    models.DateField(
                        blank=True, null=True, verbose_name="fallecimiento"
                    ),
                ),
            ],
            options={"verbose_name_plural": "autor",},
        ),
        migrations.CreateModel(
            name="genero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(help_text="inserte un genero", max_length=200),
                ),
            ],
        ),
        migrations.CreateModel(
            name="idiomas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idioma", models.CharField(max_length=200)),
            ],
            options={"verbose_name_plural": "idiomas",},
        ),
        migrations.CreateModel(
            name="libro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                (
                    "sinopsis",
                    models.TextField(
                        help_text="ingrese una breve sinopsis", max_length=1000
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
                        max_length=13,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogo.autor",
                    ),
                ),
                (
                    "genero",
                    models.ManyToManyField(
                        help_text="seleccione un genero para este libro",
                        to="catalogo.genero",
                    ),
                ),
                (
                    "idioma",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogo.idiomas",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="libroInstance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="ID único para este libro particular en toda la biblioteca",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("impreso", models.CharField(max_length=200)),
                ("devolucion", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("m", "Maintenance"),
                            ("o", "On loan"),
                            ("a", "Available"),
                            ("r", "Reserved"),
                        ],
                        default="m",
                        help_text="Disponibilidad del libro",
                        max_length=1,
                    ),
                ),
                (
                    "libro",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogo.libro",
                    ),
                ),
            ],
            options={"ordering": ["devolucion"],},
        ),
    ]
