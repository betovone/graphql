from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField("titulo", max_length=50)
    description = models.CharField("descripción", max_length=250)
    create_at = models.CharField("creado", max_length=20)
    tipo_post_id = models.ForeignKey("TipoPost", verbose_name="Tipo post", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"""
            id: {self.id}
            titulo: {self.title}
            descripcion: {self.description}
            creado: {self.create_at}
    """

class TipoPost(models.Model):
    description = models.CharField("Descripcion", max_length=150)
    
    def __str__(self) -> str:
        return f"Descripción: {self.description}"

