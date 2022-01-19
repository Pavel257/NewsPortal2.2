from django.urls import path
from .views import *

urlpatterns = [
    # path('<int:pk>', PostsDetail.as_view()),
    path('', NewsList.as_view(), name='news1'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('create/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),

]