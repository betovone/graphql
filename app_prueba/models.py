from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField("titulo", max_length=50)
    description = models.CharField("descripción", max_length=250)
    create_at = models.DateField("creado", auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"""
            id: {self.id}
            titulo: {self.title}
            descripcion: {self.description}
            creado: {self.create_at}
    """

