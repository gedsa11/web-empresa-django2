from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    #print('tipo de solicitud {}'.format(request.method))
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #suponemos que todo ha saludo bien hasta aqui
            email = EmailMessage(
                'La caffeteria: Nuevo Mensaje de contacto',
                "De {} <{}> \n\nEscribió:\n\n {}".format(name, mail, content),
                'no-contestar@inbox.mailtrap.io',
                ['gedsa2012@gmail.com'],
                reply_to=[mail]
            )
            try:
                #todo ha ido bien
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                #algo ha fallado
                return redirect(reverse('contact')+'?fail')



    return render(request, 'contact/contact.html', {'form':contact_form})