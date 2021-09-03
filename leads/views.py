from django.shortcuts import render
from django.views import generic
from .models import Lead
from django.urls import reverse
from . import forms

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"

    def get_queryset(self):
        return Lead.objects.all()

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"

    def _get_queryset(self):
        return Lead.objects.all()

class LeadUpdate(generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = forms.LeadCreateForm

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = forms.LeadCreateForm

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
