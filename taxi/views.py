from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Driver, Car, Manufacturer


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("username", "")
        if search_query:
            queryset = queryset.filter(username__icontains=search_query)
        return queryset


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("model", "")
        if search_query:
            queryset = queryset.filter(model__icontains=search_query)
        return queryset


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("name", "")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset
