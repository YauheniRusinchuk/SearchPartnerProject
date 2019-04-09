from django.urls import path, include
from .views import MainView

app_name = 'main'

urlpatterns = [
    path('article/', include('src.apps.article.urls', namespace='article')),
    path('jobs/', include('src.apps.jobs.urls', namespace='jobs')),
    path('ideas/', include('src.apps.ideas.urls', namespace='ideas')),
    path('searchpartners/', include('src.apps.search_partner.urls', namespace='search_partner')),
    path('new/', include('src.apps.new.urls', namespace='new')),
    path('register/', include('src.apps.register.urls', namespace='register')),
    path('logout/', include('src.apps.logout.urls', namespace='logout')),
    path('login/', include('src.apps.login.urls', namespace='login')),
    path('profiles/', include('src.apps.profiles.urls', namespace='profiles')),
    path('', MainView.as_view(), name='main_page'),
]
