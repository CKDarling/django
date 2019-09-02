from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,
                                    DeleteView)

from django.http import HttpResponse
from . import models
# Create your views here.
# def index(request):
    # return render(request,'index.html')

#class CBView(View):
#    def get(self,request):
#        return HttpResponse('CLASS BASED VIEWS ARE RAD')

class IndexView(TemplateView):
    template_name = 'index.html'

    #def get_context_data(self,**kwargs):
        #context = super().get_context_data(**kwargs)
        #context['inject_me'] ='BASIC INJECTION'
        #return context

class SchoolList(ListView):
    context_object_name = 'schools'
    model=models.School


class SchoolDetail(DetailView):
    context_object_name = 'school_detail'
    model=models.School
    template_name='adv_app/school_detail.html'

# CRUD items
class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    # fields are used to determine what you can alter in the model
    model=models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("adv_app:list")
