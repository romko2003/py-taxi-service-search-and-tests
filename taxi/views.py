from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Driver, Car, Manufacturer
from .forms import DriverForm, DriverLicenseUpdateForm, CarForm


def index(request):
    return render(request, "taxi/index.html")


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("username", "")
        return queryset.filter(username__icontains=query)


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("model", "")
        return queryset.filter(model__icontains=query)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("name", "")
        return queryset.filter(name__icontains=query)
