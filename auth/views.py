from django.shortcuts import render
from django.views.generic import TemplateView

# Home page
class HomeView(TemplateView):
    template_name = "auth/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context
    
# Login page
class LoginView(TemplateView):
    template_name = "auth/login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context
    
    # Handle POST request for logging in
    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
        