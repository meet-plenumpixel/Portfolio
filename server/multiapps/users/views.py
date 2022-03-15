# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib import messages
from django.contrib.auth import views as auth_view
from django.views.generic import edit as edit_view
from django.views.generic import TemplateView, DetailView
# from django.views.generic.edit import CreateView
from users import models as user_model
from users import forms as user_form

# Create your views here.



class UserProfileView(TemplateView):
  template_name = 'home/index.html'


class UserDetailView(DetailView):
  model = user_model.ProfileModel
  template_name = 'users/user_detail.html'
  context_object_name = 'profile'

  # def get_context_data(self, **kwargs):
  #   return super().get_context_data(**kwargs)


  def get(self, request, *args, **kwargs):
    self.kwargs[self.pk_url_kwarg] = self.request.user.profilemodel.pk
    print(self.kwargs[self.pk_url_kwarg])
    return super().get(request, *args, **kwargs)

  # def get_object(self, queryset=None):
  #   print()
  #   temp = super().get_object(queryset)
  #   return temp







# class UserRegisterView(CreateView):
#   form_class = user_form.UserRegisterForm
#   template_name = 'users/register.html'
#   success_url = reverse_lazy('login')


class UserLoginView(auth_view.LoginView):
  template_name = 'home/login.html'
  next_page = reverse_lazy('profile')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # print(f"{self.request.headers['Origin'] = }")
    print(f"{self.request.META.get('HTTP_REFERER') = }")
    return context

class UserLogoutView(auth_view.LogoutView):
  template_name = 'home/logout.html'


class UserRegisterView(edit_view.CreateView):
  form_class = user_form.UserRegisterForm
  template_name = 'home/register.html'
  success_url = reverse_lazy('login')
