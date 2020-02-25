"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path


from .views import (
    blog_list_view,
    blog_detail_view,
    blog_create_view,
    ArticleListView,
    ArticleDetailView
)

app_name = 'blog'
urlpatterns = [
    path('<int:my_id>/', blog_detail_view, name='blog-detail'),
    path('', blog_list_view, name='blog-list'),
    path('create/', blog_create_view, name='blog-create'),

    path('classviews/', ArticleListView.as_view(), name='article-list'),
    path('classviews/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'), #muss pk als key nehmen, da im Model standardmässig id = pk definiert ist (primary key), falls anderer key möchte, siehe 3:14
]
