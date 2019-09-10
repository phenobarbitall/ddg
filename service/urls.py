from django.urls import path

from service.views import UserList, UserRetrieve, UsernameList, UserCount

urlpatterns = [
    path('user-profiles/', UserList.as_view()),
    path('user-profile/<int:pk>/', UserRetrieve.as_view()),
    path('user-list/', UsernameList.as_view()),
    path('total-users/', UserCount.as_view())
]
