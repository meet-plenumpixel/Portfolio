from django.urls import path
from users import views as user_views


urlpatterns = [
  path('profile/', user_views.UserProfileView.as_view(), name='profile'),
  path('profile-detail/', user_views.UserDetailView.as_view(), name='profile_detail'),
  path('profile-list/', user_views.UserListView.as_view(), name='profile_list'),
  path('login/', user_views.UserLoginView.as_view(), name='login'),
  path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
  path('register/', user_views.UserRegisterView.as_view(), name='register'),

]
