from django.urls import path
from django.contrib import admin
from translation.views import api_article_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/articles/', api_article_list, name='api_article_list'),
]
