from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.

def home_view2(*args, **kwargs): #mit *args und **kwargs können eine beliebige anzahl parameter übergeben werden, die dann
                                #in args (tuple) respektive kwargs (dictionary) gespeichert sind.
                                #kann auch anders benennen, z.B. *meineparameter, entscheidend sind die
                                #UNPACKING OPERATOR * repsektive **
    return HttpResponse("<h1>Hello World22</h1>")  # string of HTML code


# def product_create_view(request): #mit pure django-form (RawProductForm
#     my_form = RawProductForm() #bei request.GET!!! (kriegt wohl nichts in request.GET)   #create instance of the form (in order to render it out)
#
#     if request.method == "POST": #if it's POST (nach ausfüllen, submit), pass in request.POST data um form zu initialisieren, für automatische (django) validation-Prüfung
#         my_form = RawProductForm(request.POST) #create an Instance of the form (macht bereits die Validierung?! falls von Hand required-Field im HTML löscht und dann form leer abschickt, server sendet automatisch form nochmals zurück mit 'This field is required' Hinweis, und da neu gerendert wird ist required-Attribut auch wieder drin)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render (request, "products/product_create.html", context)

def product_create_view(request): #mit model_form (ProductForm)
    #print(request.GET)
    #print(request.POST)
    #my_new_title = request.POST.get('title')
    #Product.objects.create(title=my_new_title)

    form = ProductForm(request.POST or None) #im Falle von None (get) rendert einfach ein leeres Formular
    if form.is_valid():
        form.save()
        form = ProductForm() #leeres Formular rendern/laden nach Speichern

    context = {
        'form': form
    }
    return render (request, "products/product_create.html", context)


def render_initial_data(request):
    #Einem (mehreren) Field initial data mitgeben!!!
    initial_data = {
        'title': "My awesome title"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    #------- ODER-------
    # #Data von einem existierenden Objekt anzeigen, Änderungen werden dann wieder in dieses Objekt gespeichter
    # # kann Objekt natürlich auch dynamsich auslesen...
    # obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request): #zeigen details von einem product
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render (request, "products/product_detail.html", context)


def dynamic_lookup_view(request, my_id): #get an attribute my_id form the URL (siehe urls.py)
    #obj = Product.objects.get(id=my_id)

    obj = get_object_or_404(Product, id=my_id) #gibt 404 statt irgendein Query-Error aus, falls es für id im URL kein entsprechendes Product gibt..
    #ODER
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist: # die Exception die die Linie oben wirft, falls id nicht gibt
    #     raise Http404

    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object":obj
    }

    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)