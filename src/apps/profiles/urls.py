from django.urls import path
from .views import ProfilesView, ProfileDetail, UpdateProfile

app_name = 'profiles'


urlpatterns = [
    path('', ProfilesView.as_view(), name='profiles_all'),
    path('<str:name>/id<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('<str:name>/id<int:pk>/update/', UpdateProfile.as_view(), name='profile_update'),
]
