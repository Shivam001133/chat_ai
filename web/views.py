from datetime import datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from users.user_authenticate import UserAuthenticate


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        heading_data = 'Your Virtual Companion'
        sub_heading_data = 'Connecting You to a World of Possibilities'
        data = {
            'main_heading': heading_data,
            'sub_heading': sub_heading_data
        }
        context['heading'] = data

        return context


class LoginPage(TemplateView):
    template_name = 'login.html'


class ProfilePage(TemplateView):
    template_name = 'profile.html'

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("email: ", email, '\n', "password: ", password)

        user = UserAuthenticate(email, password)

        if user is not None:
            login(request, user)
            data = {
                'user_name': user.first_name
            }
            context['user'] = data
            return render(request, 'profile.html', context)
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login-page')

    def get(self, request, **kwargs):
        return render(request, 'login.html')
