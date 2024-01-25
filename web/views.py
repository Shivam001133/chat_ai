from datetime import datetime
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView


def your_view(request):
    current_year = datetime.now().year
    context = {
        'base_data': {
            'current_year': current_year
        }
    }
    return render(request, 'base.html', context)


class HomePage(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs: Any):
    #     data = super().get_context_data(**kwargs)
    #     return redirect('index.html')


def login_page_view(request):
    return render(request, 'login.html')


def new_login(request):
    url = reverse('login-page')
    return redirect(url)


def profile_page_view(request, roll):
    return HttpResponse(f"his is {roll}")
