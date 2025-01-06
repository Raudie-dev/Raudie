from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print(f"Nombre: {name}, Email: {email}, Mensaje: {message}")  # Para depurar
        
        # Enviar correo
        try:
            send_mail(
                subject,
                f'Mensaje de {name} <{email}>:\n\n{message}',
                'juanxcosa@gmail.com',  # Cambia esto por tu correo
                ['juandiegoaranaperez@gmail.com'],  # Cambia esto por el correo del destinatario
                fail_silently=False,
            )
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('index')  # Redirige a la vista de índice
        except Exception as e:
            print(e)  # Imprimir el error para depurar
            messages.error(request, 'Hubo un error al enviar tu mensaje. Inténtalo de nuevo.')

    return render (request, "index.html")