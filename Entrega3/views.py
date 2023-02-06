from django.http import HttpResponse
from django.template import Template,Context,loader

def saludo(request):
    return HttpResponse ("Bienvenido a Mendoza")

def prueba(request):

    nombre= "Profe"

    pais= "Argentina"

    diccionario= {"name":nombre, "country":pais}
    
    """
    miHtml=open("C:/Users/Gustavo/Desktop/ENTREGAS/Entrega3/Entrega3/plantillas/plantilla1.html")

    plantilla= Template(miHtml.read())

    miHtml.close()

    miContexto= Context(diccionario)

    documento= plantilla.render(miContexto)
    """

    plantilla=loader.get_template("plantilla1.html")

    documento= plantilla.render(diccionario)
    
    return HttpResponse(documento)
    