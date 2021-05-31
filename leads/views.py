from django.shortcuts import render, redirect, reverse
from .models import Lead
from .forms import LeadModelForm
from django.views import generic

# Create your views here.

class LeadListView(generic.ListView):
    template_name = 'leads/home_page.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


def lead_list(request):
    leads = Lead.objects.all()
    
    context = {
        "leads": leads
    }
    return render(request, 'leads/home_page.html', context)

class LeadDetailView(generic.DetailView):
    queryset = Lead.objects.all()
    template_name = 'leads/detail_page.html'
    context_object_name = 'lead'

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    
    context = {
        'lead': lead
    }
    return render(request, 'leads/detail_page.html', context)

class LeadCreateView(generic.CreateView):
    template_name = 'leads/create_lead.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:home")

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/leads')
    
    context = {
        'form': form
    }
    return render(request, 'leads/create_lead.html', context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    
    context = {
        'form': form
    }

    return render(request, 'leads/update_lead.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')