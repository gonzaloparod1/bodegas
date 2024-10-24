
1. Models Principales 

    - User <- auth.User
        - username 
        - password 
        - email 
        - first_name 
        - last_name 
        - is_active 
        - is_authenticated 
    - UserProfile <- extender la info del USUARIO que no solicitan
        - direccion 
        - bigrafía 
        - fecha_nac 
        - rol || tipo_usuario 
    - ListaProductosServicios  
        - nombre 
        - descripcion 
    - Contacto || Solicitud 
        - mensaje 
        - data_identidad de quien nos quiere contactar o solicitar el producto / servicio 

- OPCIONES de INICIO "/"
    - REGISTRARME - INICIAR SESIÓN (2 form o uno con las dos opciones)    
    - LandingPage 
    - Página de Inicio -> Lista - NavBar || SlideBar - Footer
        - base.html -> extends index.html (contiene la LISTA de lo que ofrecemos <- ListaProductosServicios)

**Si la sesión se encuentra abierta vamos a "/" <- que es la Lista + base.html, de lo contrario vamos a "/login" + registro**







