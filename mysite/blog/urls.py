
from blog import views
from django.urls import path



urlpatterns=[
     path("",views.PostListView.as_view(),name="post_list"),
     path('about/', views.AbouView.as_view(),name="about"),
     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
     path('post/new',views.CreatePostView.as_view(),name='post_new'),
     path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
     path('post/<int:pk>/remove', views.PostDeleteView.as_view(), name='post_remove'),
     path('drafts', views.DraftListView.as_view(), name='post_draft_list'),
     path('post/<int:pk>/',views.add_comment_to_post,name='add_comment_to_post')
]