from django.shortcuts import render, redirect, reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm

# Create your views here.


def contact(request):
    """ A view to return the contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            message = request.POST.get('message')
            contact_email = request.POST.get('email')
            form.save()

            email = EmailMessage(
                "New contact form submited at Henrique Peroni website",
                'You have a new contact form available to you on '
                f'henriqueperoni.com from {contact_email}. \n\n\n \
                    Customer Query:'
                f'\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                reply_to=[contact_email],
            )
            try:
                email.send(fail_silently=False)
                messages.success(request, 'Email successful sent.')
            except Exception as e:
                print(f'Email failed, error: {e}')
            return redirect(reverse('contact'))
        else:
            print('Form invalid')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
