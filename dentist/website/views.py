from django.shortcuts import render
from django.core.mail import send_mail
import threading



# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name'] 
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        def mailer(name, email, phone, message):
            send_mail(
                name,# subject
                message +" "+ phone, # message
                email, #from email
                ['devphase254@gmail.com', 'kanjurus8@gmail.com', 'kanjurus30@gmail.com'], # to email
                    )
        t1 = threading.Thread(target=mailer, args=(name, email, phone, message))
        t1.start()
        return render(request, 'home.html', {'name':name })
    else:
        return render(request, 'home.html', {})