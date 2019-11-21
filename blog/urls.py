from django.urls import path
from .views import PersonListView, PersonDetailView

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='get_post_person'),
    path('persons/<int:pk>', PersonDetailView.as_view(), name='get_put_delete_person'),
]