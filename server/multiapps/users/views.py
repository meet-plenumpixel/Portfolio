# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView, ListView
from users import models as user_model
from users import forms as user_form

# Create your views here.



class UserProfileView(TemplateView):
  template_name = 'home/index.html'


class UserDetailView(DetailView):
  model = user_model.ProfileModel
  template_name = 'users/user_detail.html'
  context_object_name = 'profile'

  def get(self, request, *args, **kwargs):
    self.kwargs[self.pk_url_kwarg] = self.request.user.profilemodel.pk
    print(self.kwargs[self.pk_url_kwarg])
    return super().get(request, *args, **kwargs)


class UserListView(ListView):
  model = user_model.ProfileModel
  template_name = 'users/user_list.html'
  context_object_name = 'users_profile'












class UserLoginView(LoginView):
  template_name = 'home/login.html'
  next_page = reverse_lazy('profile')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # print(f"{self.request.headers['Origin'] = }")
    print(f"{self.request.META.get('HTTP_REFERER') = }")
    return context

class UserLogoutView(LogoutView):
  template_name = 'home/logout.html'


class UserRegisterView(CreateView):
  form_class = user_form.UserRegisterForm
  template_name = 'home/register.html'
  success_url = reverse_lazy('login')
