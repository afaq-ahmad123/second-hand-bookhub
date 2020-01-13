from django.shortcuts import render, redirect
from django.conf import settings
from django.apps import apps
from django.contrib import messages
from .forms import add_book
#from user.models import user as userInfo
from django.core.files.storage import FileSystemStorage
#
# from uploads.core.models import Document
# from uploads.core.forms import DocumentForm
# Create your views here.
userInfo = apps.get_model('login','user');
book = apps.get_model('home','book')
def sale(request):
    form = add_book(request.POST or None)
    if 'email' in request.session:
        email = request.session['email']
        user = userInfo.objects.get(email=email)
        form.sellerID = user.id
        print("session OK")
    else:
        user = userInfo.objects.get(email="kashifsss915@gmail.com")
        form.sellerID = user.id
        return redirect('login_user')
    print(form)
    if request.method == "POST":
        print("Image selected OK")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        form.image = uploaded_file_url
    if request.method == "POST":
        print("request OK")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print("form Saved")
        form.save()
        messages.add_message(request, messages.INFO, "Book uploaded successfully!{{ uploaded_file_url }}")
        #return render(request, 'sell/sale.html', {
         #   'uploaded_file_url': uploaded_file_url, 'form': form, 'user': user, 'message': messages})
        print(form.sellerID, form.title)
        return redirect('home-url')
    return render(request,'sell/sale.html', {'form': form, 'user': user, 'message': messages})

def add(request):
    bookForm = add_book(request.POST or None)
    form=book(title='Computer Science with C++',price='56',writer='Michael Winston')
    form.save()
    return render(request, 'sell/sale.html', {'form': form})
#
# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home-url')
#     else:
#         form = DocumentForm()
#     return render(request, 'sell/model_forms.html', {
#         'form': form
#     })
