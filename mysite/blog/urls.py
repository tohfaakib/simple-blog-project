from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    re_path('post/(?P<pk>\d+)/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    re_path('post/edit/(?P<pk>\d+)/', views.PostUpdateView.as_view(), name='post_edit'),
    re_path('post/remove/(?P<pk>\d+)/', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftPostList.as_view(), name='post_draft_list'),
    path('about/', views.AboutView.as_view(), name='about'),

    re_path('post/comment/(?P<pk>\d+)/', views.add_comment_to_post, name='add_comment_to_post'),
    re_path('comment/approve/(?P<pk>\d+)/', views.comment_approve, name='comment_approve'),
    re_path('comment/delete/(?P<pk>\d+)/', views.comment_remove, name='comment_remove'),
    re_path('post/publish/(?P<pk>\d+)/', views.post_publish, name='post_publish'),

]