from django.urls import path
from django.contrib import admin
from translation.views import ArticleListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('articles/', ArticleListView.as_view(), name='api_article_list'),
]
