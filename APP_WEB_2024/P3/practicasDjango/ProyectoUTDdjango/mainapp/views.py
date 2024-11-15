from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html',{
        'tittle':'Inicio',
        'content':'Bienvenido a mi pagina de incio',
    })

def acercade(request):
    return render(request,'mainapp/about.html',{
        'tittle':'Acerca de'
    })

def mision(request):

    return render(request,'mainapp/mision.html',{
        'tittle':'Mision',
    })

def vision(request):
    #HttpResponse(html)
    return render(request,'mainapp/vision.html',{
        'tittle':'Vision',
    })

#Redirigir a la página inicio con error 404    
""" def redireccion_index(request, exception):
    return redirect('inicio') """
    
#Redirigir a la página inicio con error 404, manera 2
def redireccion_index_2(request,exception):
    return render(request,'mainapp/404.html')