from django.db import models # type: ignore
from django.contrib.auth.models import User


#_________________________________________________________________________________________________________
# MODEL CONTACTO
class ContactForm(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
class TipoBodega(models.Model):
    tipo = models.CharField(max_length=255)
    metros_cuadrados = models.PositiveIntegerField()
    quimicos = models.BooleanField(default=False)
    organicos = models.BooleanField(default=False)
    hermetica = models.BooleanField(default=False)
    precio_mensual = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.metros_cuadrados}m²"


class Bodega(models.Model):
    codigo = models.CharField(max_length=10)
    tipo_bodega = models.ForeignKey(TipoBodega, on_delete=models.CASCADE, related_name='bodegas')
    disponible = models.BooleanField(default=True)  # Nueva propiedad para manejar la disponibilidad
    def __str__(self):
        return f"Bodega {self.codigo} ({self.tipo_bodega.tipo})"


class Noticia(models.Model):
    titulo = models.CharField(max_length=45)
    cuerpo = models.TextField()
    imagen_url = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


class Like(models.Model):
    # user_id <- no es necesario tipear user_id al igual con noticia_id
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"Like by user {self.user_id} on {self.noticia.titulo}"




#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

"""
* class TipoBodega(models.Model):
id  int
tipo varchar 255
metros int  cuadrados (entero positivo)
quimicos  (boolean)
organicos (boolean)
hermetica (boolean)
precio_mensual (entero positivo)

* class Bodega(models.Model):
id
codigo varchar 10 
tipo_bodega int   FK relacion de 1:N

* class Noticia(models.Model):
id int
titulo varchar 45 
cuerpo text 
imagen_url varchar 255

* class Like(models.Model):
id 
user_id int     1:N
noticia_id int  1:N
"""
