from django.urls import path
from .views import NippoListView ,NippoDetailView, NippoCreateModelFormView,NippoUpdateModelFormView, NippoCreateFormView, nippoListView, nippoDetailView, nippoCreateView, nippoUpdateFormView, nippoDeleteView
 
urlpatterns = [
  path("", NippoListView.as_view(), name="nippo-list"),
  path("detail/<int:pk>/", NippoDetailView.as_view(), name="nippo-detail"),
  # path("create/", NippoCreateModelFormView.as_view(), name="nippo-create"),
  path("create/", nippoCreateView, name="nippo-create"),
  path("update/<int:pk>/", NippoUpdateModelFormView.as_view(), name="nippo-update"),
  path("delete/<int:pk>/", nippoDeleteView, name="nippo-delete"),
]

