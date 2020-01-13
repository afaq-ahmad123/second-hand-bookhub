from django.shortcuts import render, redirect
from django.contrib import messages

from django.apps import apps
userInfo = apps.get_model('login','user')
def rate(y):
    rate=[]
    for x in range(5):
        if x in range(y):
            rate.append(True)
        else:
            rate.append(False)
    return rate

featured = [
    {
        'seller' : 'Michael Winston',
        'seller_id' : '1089772',
        'seller_pic' : "/media/images/profile/me.jpg",
        'featured' : True,
        'rating' : rate(4),
        'book_img' : '/media/images/home/book1.jpg',
        'book_price' : '$56',
        'book_name' : 'Computer Science with C++'
    },
]

# Create your views here.
def home(request):
    context = {
        'features' : featured
    }
    if 'email' in request.session:
        email = request.session['email']
        user = userInfo.objects.get(email=email)
        return render(request,'home/home.html', {'features' : featured, 'user': user})
    else:
        return redirect("login")

def detail(request, book):
    obj = featured[int(book)-1]
    messages.error(request, 'Book is uploading!', extra_tags='alert', fail_silently=True)
    context = {
        'book' : obj
    }
    if 'email' in request.session:
        email = request.session['email']
        user = userInfo.objects.get(email=email)
        return render(request,'home/detail.html', {'book' : obj, 'user': user})
    else:
        return redirect("login")

def cart(request):
    return render(request,'home/cart.html')
