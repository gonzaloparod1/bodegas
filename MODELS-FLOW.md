
```py
class UserProfile(models.Model):
    TIPOS_USUARIOS = (('normal', 'Normal'), ('premium', 'Premium'))
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=255, choices=TIPOS_USUARIOS, default='normal')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.tipo_usuario})'

class Producto(models.Model):
    CATEGORIAS = (('hogar', 'Hogar'), ('deporte', 'Deporte'))
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    categoria = models.CharField(max_length=255, choices=CATEGORIAS, default='hogar')
    stock = models.BooleanField(default=True)
    usuarios = models.ManyToManyField(User, related_name='productos')

#* TABLA INTERMEDIA ProductoUser
```

