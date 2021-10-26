from django.shortcuts import render
from django.views.generic import ListView, DetailView
from slider.models import Slider


class SliderListView(ListView):
    model = Slider
    template_name = 'store/index.html'
    # template_name = 'store/test.html'
    context_object_name = 'sliders'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
