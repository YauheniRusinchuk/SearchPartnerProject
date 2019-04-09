from django.urls import path
from .views import ArticleDetail, UpdateArticle, DeleteArticle

app_name = 'article'


urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view(), name='article_page'),
    path('<int:pk>/update/', UpdateArticle.as_view(), name='article_update'),
    path('<int:pk>/delete/', DeleteArticle.as_view(), name='article_delete')
]
