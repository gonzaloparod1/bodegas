from django.contrib import admin
from .models import Noticia, Bodega, ContactForm, TipoBodega, Like
# Register your models here.

admin.site.register(Noticia)
admin.site.register(Bodega)
admin.site.register(TipoBodega)
admin.site.register(Like)
admin.site.register(ContactForm)