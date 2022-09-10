from django.urls import path

from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
   path('', UserListCreateView.as_view()),
   path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view())

]