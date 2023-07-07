# at the top of the file import reverse 
from django.urls import reverse
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView
# import models
from .models import Cuisine
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView, UpdateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

#...
class About(TemplateView):
    template_name = "about.html"

class CuisineList(TemplateView):
    template_name = "cuisine_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["cuisines"] = Cuisine.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["cuisines"] = Cuisine.objects.all()
             # default header for not searching 
            context["header"] = "Popular Cuisines"
        return context

class CuisineCreate(CreateView):
    model = Cuisine
    fields = ['name', 'img', 'bio']
    template_name = "cuisine_create.html"
     # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('cuisine_detail', kwargs={'pk': self.object.pk})

class CuisineDetail(DetailView):
    model = Cuisine
    template_name = "cuisine_detail.html"

class CuisineUpdate(UpdateView):
    model = Cuisine
    fields = ['name', 'img', 'bio']
    template_name = "cuisine_update.html"
    def get_success_url(self):
        return reverse('cuisine_detail', kwargs={'pk': self.object.pk})

class CuisineDelete(DeleteView):
    model = Cuisine
    template_name = "cuisine_delete_confirmation.html"
    success_url = "/cuisines/"