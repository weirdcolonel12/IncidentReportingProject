from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ReportingForm
from .models import ReportingModel
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
import json
import datetime
# Create your views here.

class IndexView(TemplateView):
	template_name = 'html/index.html'





def reporting(request):
	if request.method == 'POST':
		form = ReportingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = ReportingForm
	return render(request, 'html/app-form.html',{'form': form,})
