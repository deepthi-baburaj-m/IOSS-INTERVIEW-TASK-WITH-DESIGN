
from django.shortcuts import render, redirect, get_object_or_404
import string
import random
from .forms import URLForm
from .models import URL
from django.contrib import messages

#Function to generate shorter url
def create_shorter_url(length=6):
    shorter_url=''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return shorter_url


#Function to get the lengthy url and convert it into shorter one
def index(request):
    short_url = None
    #Checks whether the metho is POST or not
    if request.method == 'POST':
        #Getting the datas from html through Form
        form = URLForm(request.POST)
        #Checks whether the form is valid or not
        if form.is_valid():
            #Getting the original url 
            original_url = form.cleaned_data['original_url']
            # Check if the URL already exists or not , If not creating one
            obj, created = URL.objects.get_or_create(original_url=original_url)
            #If object is already created, updating the shorter url
            if created:
                obj.shorter_url = create_shorter_url()
                obj.save()
            short_url = request.build_absolute_uri(f"/{obj.shorter_url}")
        else:
            messages.info(request,"Something went wrong")
    else:
        form = URLForm()
    return render(request, 'index.html', {'form': form, 'short_url': short_url})

def redirect_url(request, shorter_url):
    url = get_object_or_404(URL, shorter_url=shorter_url)
    return redirect(url.original_url)