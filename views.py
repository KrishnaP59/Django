from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import smartphone,laptop
from .form import smartphoneForm,laptopForm


def index(request):
    return render(request,'index.html')


def display_smartphone(request):
    products = smartphone.objects.all()
    context = {
        "products" : products,
        "header" : "smartphone",
    }
    return render(request,"index.html", context)


def display_laptop(request):
    products = laptop.objects.all()
    context = {
        "products" : products,
        "header" : "laptop",
    }
    return render(request,"index.html", context)

def add_device(request,fm):
    if request.method == "POST":
        form = fm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = fm()
        return render(request, 'add.html', {'form' : form})


def add_smartphone(request):
    return add_device(request, smartphoneForm)


def add_laptop(request):
    return add_device(request, laptopForm)



def edit_smartphone(request,pk):
    products = get_object_or_404(smartphone,pk=pk)
    if request.method == "POST":
        form = smartphoneForm(request.POST,instance = products)

        if form.is_valid():
            form.save()

            return redirect('index')
        else:
            form = smartphoneForm(instance = products)

            return render(request,'edit.html',{'form':  form})



def edit_laptop(request,pk):
    products= get_object_or_404(laptop, pk=pk)

    if request.method == "POST":
        form = laptopForm(request.POST,instance = products)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            form = laptopForm(instance = products)
            return render(request, 'edit.html', {'form': form})


def delete_smartphone(request,pk):
    smartphone.objects.filter(id=pk).delete()

    products = smartphone.objects.all()
    context = {
        "products": products
    }
    return render(request,"index.html",context)

def delete_laptop(request,pk):
    laptop.objects.filter(id=pk).delete()

    products = laptop.objects.all()
    context = {
        "products": products
    }
    return render(request,"index.html",context)
