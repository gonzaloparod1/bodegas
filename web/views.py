from django.shortcuts import render, redirect, get_object_or_404
# from .services import 
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ContactModelForm, UserForm, CotizacionForm
from .models import ContactForm, Noticia, Like, TipoBodega, Bodega
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
#TODO__ Vista para Cotización
@login_required
def cotizar(request):
    # Obtener bodegas ya seleccionadas desde la sesión
    bodegas_cotizadas = request.session.get('bodegas_cotizadas', [])
    
    # Lista de tipos de bodega que tienen bodegas disponibles
    # tipo_bodegas = TipoBodega.objects.filter(bodegas__disponible=True) # <- trae tantos tipos tantas bodegas tengamos
    
    tipo_bodegas = TipoBodega.objects.filter(bodegas__disponible=True).distinct()
    
    # Camino simple
    result_tipos = TipoBodega.objects.all()
    result_tipos = [tipo for tipo in result_tipos if tipo.bodegas.filter(disponible=True).exists()]
    print(f'01 - {tipo_bodegas}')
    print(f'02 - {result_tipos}')

    if request.method == 'POST':
        tipo_bodega_id = request.POST.get('tipo_bodega')
        if tipo_bodega_id:
            # Buscar el primer tipo de bodega disponible
            tipo_bodega = get_object_or_404(TipoBodega, pk=tipo_bodega_id)
            bodega_disponible = Bodega.objects.filter(tipo_bodega=tipo_bodega, disponible=True).first()
            
            if bodega_disponible:
                # Marcar bodega como no disponible
                bodega_disponible.disponible = False
                bodega_disponible.save()
                
                # Agregar bodega seleccionada a la lista de la sesión
                bodegas_cotizadas.append({
                    'id': bodega_disponible.id,
                    'codigo': bodega_disponible.codigo,
                    'tipo': bodega_disponible.tipo_bodega.tipo,
                    'precio_mensual': bodega_disponible.tipo_bodega.precio_mensual
                })
                request.session['bodegas_cotizadas'] = bodegas_cotizadas
                return redirect('cotizar')  # Recargar la página para mostrar la nueva lista

    return render(request, 'cotizar.html', {
        'tipo_bodegas': result_tipos,
        'bodegas_cotizadas': bodegas_cotizadas,
    })

#TODO__ Vista para el Resultado de la Cotización
@login_required
def resultado_cotizacion(request):
    bodegas_cotizadas = request.session.get('bodegas_cotizadas', [])
    total = sum([bodega['precio_mensual'] for bodega in bodegas_cotizadas])
    
    # Actualiza la disponibilidad de las bodegas a True
    for bodega in bodegas_cotizadas:
        # Suponiendo que bodega tiene un atributo 'id' que corresponde al ID de la bodega
        bodega_obj = Bodega.objects.get(id=bodega['id'])
        bodega_obj.disponible = True
        bodega_obj.save()
        
    # Limpia bodegas_cotizadas del request.session    
    request.session['bodegas_cotizadas'] = []
    
    return render(request, 'resultado_cotizacion.html', {
        'bodegas_cotizadas': bodegas_cotizadas,
        'total': total
    })




#TODO__ INGRESO PRINCIPAL del USUARIO - MANEJO de LÓGICA SOLICITADA por el CLI (dueño) de como INICIA la APP 


def index(request):
    noticias = Noticia.objects.all()
    user_likes = []
    
    # Obtenemos los likes del usuario si está logeado
    if request.user.is_authenticated:
        user_likes = Like.objects.filter(user=request.user).values_list('noticia_id', flat=True)
        #todo_ .values_list('noticia_id', flat=True):
        # Toma los resultados de la consulta filtrada y extrae solo los valores de la columna noticia_id.
        # flat=True significa que se devolverá una lista plana en lugar de una lista de tuplas.
        
        #* el html implementado -> {% if n.id in user_likes %}
    
    return render(request, 'index.html', {'noticias': noticias, 'user_likes': user_likes})


@login_required
def like(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    user = request.user
    
    # Verifica si el usuario ya dio like a esta noticia
    like, created = Like.objects.get_or_create(user=user, noticia=noticia)
    
    if not created:
        # Si el like ya existe, lo eliminamos (esto podría actuar como "quitar like")
        like.delete()
    
    return redirect('home')

#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████


#* FORM de Registro
#TODO__ REGISTER  - FORMS
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form} )

#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████


#* VER PERFIL
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile_detail.html', {
        'user': user,
    })

#* EDITAR PERFIL 
@login_required
def edit_profile_view(request):
    user = request.user 
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else: 
        user_form = UserForm(instance=user) 
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
    })


def about(request):
    return render(request, 'about.html', {})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        print(f'errors -> {form.errors}')
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            messages.success(request, f'Gracias por contactarse con nosotros, en breve le responderemos.')
            return redirect('home')
    else: 
        form = ContactModelForm()   
    return render(request, 'contact.html', {'form':form})


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

