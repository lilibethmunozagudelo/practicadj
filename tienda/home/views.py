from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, me encuentro en la aplicaciòn home")

def home(request):
    return HttpResponse("Hola, esta es una nueva funciòn home")