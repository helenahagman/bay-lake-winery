from django.shortcuts import render


class Home(generic.TemplateView):
    # Opens start page
    template_name = "index.html"
