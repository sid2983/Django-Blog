from django.urls import path
from . import views
app_name = 'djblog'

urlpatterns = [
    # path('',views.RoomListView.as_view(),name='djblog-rooms'),
    path('', views.HomeView.as_view(), name='djblog-home'),
    path('rooms/<int:pk>/', views.PostByRoomListView.as_view(), name='djblog-post-by-room'),
    path('editors/', views.EditorDetails.as_view(), name='djblog-editors'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='djblog-post-detail'),
    path('post/new/',views.PostCreateView.as_view(),name='djblog-post-create'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name='djblog-post-update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='djblog-post-delete'),
    path('about/',views.about, name='djblog-about'),
    path('new/',views.newpage,name='new-page')
    # path('rooms/<int:pk>/',views.room_authors,name='room_authors')
    
] 

