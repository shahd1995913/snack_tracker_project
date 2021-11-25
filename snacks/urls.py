from snacks.views import SnackListView, SnackDetailView

from django.urls import path


urlpatterns = [

    path('', SnackListView.as_view(), name='snacks_list'),



    path('<int:pk>', SnackDetailView.as_view(), name='snacks_details' ),

]