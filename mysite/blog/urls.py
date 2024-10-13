from django.conf.urls import url
from blog import views
from django.urls import path



urlpatterns=[
     path("/",views.PostListView.as_view(),"post_list"),
     path('about/', views.AbouView.as_view(),name="about"),
     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
     path('post/new',views.CreatePostView.as_view(),name='post_new'),
     path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
]