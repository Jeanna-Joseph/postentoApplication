from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
# class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'index.html', context=None)

# class AboutPageView(TemplateView):
#    template_name = "about.html"

# class LoginPageView(TemplateView):
def login(request):
    return render(request,'login.html')

def studentlogin(request):
    return render(request,'studentlogin.html')

def restaurantlogin(request):
    return render(request,'restaurantlogin.html')

@login_required
# class HomeView(TemplateView):
def home(request):
    return render(request, 'home.html')

