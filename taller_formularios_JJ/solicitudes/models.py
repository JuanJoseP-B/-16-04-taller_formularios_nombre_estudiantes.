from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD = [
        ('ACAD', 'Académica'),
        ('ADMIN', 'Administrativa'),
        ('TECN', 'Técnica'),
        ('OTRA', 'Otra'),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()  # Campo numérico
    tipo_solicitud = models.CharField(
        max_length=5,
        choices=TIPO_SOLICITUD,
        default='ACAD',
    )
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to='adjuntos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"