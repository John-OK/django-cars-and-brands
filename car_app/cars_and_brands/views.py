from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from . models import Brand, Car

def index(request):
    return HttpResponseRedirect('brands')

def brands(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'cars_and_brands/brands.html', context)

def brand_detail(request, id):
    brand_info = Brand.objects.get(pk=id)
    context = {'brand_info': brand_info}
    print(f"HERE'S THE brand_info: {brand_info.make}")
    return render(request, 'cars_and_brands/brand_detail.html', context)

def car_list_all(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars_and_brands/all_cars.html', context)