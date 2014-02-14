from django.db import models

# Create your models here.
class Revista(models.Model):
	nombre = models.CharField(, max_length=50)
	
	class Meta:
		verbose_name = _('Revista')
		verbose_name_plural = _('Revistas')

	def __unicode__(self):
		return self.nombre
	

class Articulo(models.Model):
    nombre = models.CharField(, max_length=50)
    comentario = models.TextField(max_length=400)
    repuesta = models.TextField(max_length=400)
    class Meta:
        verbose_name = _('Articulo')
        verbose_name_plural = _('Articulos')

    def __unicode__(self):
        return self.nombre



