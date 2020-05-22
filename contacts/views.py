from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Contact


def contact(request):
   if request.method == 'POST':
        product_id=request.POST['product_id']
        product=request.POST['product']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        user_id=request.POST['user_id']
        message=request.POST['message']
      

        # check if user has made enquiry already

        if request.user.is_authenticated:
           user_id= request.user_id
           has_contacted =Contact.objects.all.filter(product_id=product_id,user_id=user_id)
           if has_contacted:
              messages.error(request,'You have already made an Enquiry for this product')
              return redirect('/products/'+product_id)

        contact = Contact(product_id=product_id, name=name, email=email, phone=phone,message=message, user_id=user_id)

        contact.save()
        messages.success(request,'You are booking have been confirmed , order acceptenance will be confirmed soon ')
        return redirect('/products/'+product_id)

        #send mail
        
        send_mail (
            'Product booking details',
            ' There has been an Enquiry fir '+ product +' sign in to admin panel ',
            'nandeesh.tgsvt@gmail.com',
            ['nandeesh.hoysalatech@gmail.com'],
            fail_silently=False,
         )

         

         