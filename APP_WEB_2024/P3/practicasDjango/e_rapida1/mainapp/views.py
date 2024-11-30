from django.shortcuts import render, redirect

#Create your views here.
def index(request):
    return render(request,'mainapp/index.html',{
        'tittle':'Inicion | Pagina principal',
        'content':'..:: !Bienvenido a mi pagina priincipali pagina priincipal! ::..'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'tittle':'Acerca de',
        'content':'..::Somos un equipo de Desarrollo de SW con DJango::..'
    })


def mision(request):
    return render(request,'mainapp/mision.html',{
        'tittle':'Mision de la UTD',
    })


def vision(request):
    return render(request,'mainapp/vision.html',{
        'tittle':'Vision de la UTD',
    })
    
def register_user(request):
    return render(request,'mainapp/register_user.html',{
        'tittle':'Registrarse',
        'content':'Pon tus datos'
    })
    
def login_user(request):
    return render(request,'mainapp/login_user.html',{
        'tittle':'Inicio de sesión',
        'content':'Ingresa tu correo y contraseña',
    })
    
def alerta_404(request,exception):
    return render(request, 'mainapp/404.html', status=404)