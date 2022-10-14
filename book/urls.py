from django.urls import path

from book.views import index, topic_list, test_detail, slide_list, slide_detail, video_list, video_detail, edumat_list, \
    edumat_detail
from .views import topic_detail, test_list

urlpatterns = [
    path('', index, name='index'),
    path('topic_list/', topic_list, name="topic-list"),
    path('topic_detail/<int:pk>/', topic_detail, name="topic-detail"),

    path('test/', test_list, name="test-list"),
    path('test_detail/<int:pk>/', test_detail, name="test-detail"),

    path('slide/', slide_list, name="slide-list"),
    path('slide_detail/<int:pk>/', slide_detail, name="slide-detail"),

    path('video/', video_list, name="video-list"),
    path('video_detail/<int:pk>/', video_detail, name="video-detail"),

    path('edumat/', edumat_list, name="edumat-list"),
    path('edumat_detail/<int:pk>/', edumat_detail, name="edumat-detail"),
]
