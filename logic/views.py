from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from .models import Carousel, Category, List, List1, Team, Test
from .forms import ContactForm
# Create your views here.
def a404(request):
    return render(request, "404.html", context={})

def about(request):
    team = Team.objects.all()
    context = {
        "team": team,
    }
    return render(request, "about.html", context=context)

def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvafaqqiyatli amalga oshirildi!")
    context = {
        "contact": contact,
    }
    return render(request, "contact.html", context=context)

def index(request):
    test = Test.objects.all()
    team = Team.objects.all()
    list = List.objects.all()
    list1 = List1.objects.all()
    carousel = Carousel.objects.all()
    category = Category.objects.all()
    context = {
        "test": test,
        "team": team,
        "carousel": carousel,
        "category": category,
        "list": list,
        "list1": list1,
    }
    return render(request, "index.html", context=context)

def agent(request):
    test = Test.objects.all()
    context = {
        "test": test,
    }
    return render(request, "property-agent.html", context=context)

def list(request):
    list = List.objects.all()
    list1 = List1.objects.all()
    context = {
        "list": list,
        "list1": list1,
    }
    return render(request, "property-list.html", context=context)

def type(request):
    category = Category.objects.all()
    context = {
        "category": category,
    }
    return render(request, "property-type.html", context=context)

def testimonial(request):
    test = Test.objects.all()
    context = {
        "test": test,
    }
    return render(request, "testimonial.html", context=context)

def aboutdetailview(request):
    return render(request, "aboutdetail.html", context={})


def categdetailview(request, id):
    try:
        categ = Category.objects.get(id=id)
        context = {
            "categ": categ,
        }
    except categ.DoesNotExists:
        raise categ.Http404("No category found")
    return render(request, "categdetail.html", context=context)

def listdetailview(request, list):
    list = get_object_or_404(List, slug=list)
    context = {
        "list": list,
    }
    return render(request, "listdetail.html", context=context)

class listUpdateView(UpdateView):
    model = List
    fields = ('name', 'price', 'bio', 'location', 'sqft', 'bed', 'bath')
    template_name = 'listEdit.html'

class listDeleteView(DeleteView):
    model = List
    template_name = 'listDelete.html'
    success_url = reverse_lazy('index')

def teamdetailview(request, team):
    team = get_object_or_404(Team, slug=team)
    context = {
        "team": team,
    }
    return render(request, "teamdetail.html", context=context)

class teamUpdateView(UpdateView):
    model = Team
    fields = ('img', 'name', 'rank')
    template_name = 'teamEdit.html'

class teamDeleteView(DeleteView):
    model = Team
    template_name = 'teamDelete.html'
    success_url = reverse_lazy('index')

class TeamCreateView(CreateView):
    model = Team
    template_name = "teamCreate.html"
    fields = ('img', 'name', 'rank')


