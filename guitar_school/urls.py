from django.urls import path 

from guitar_school.views.index import Index
  
  
urlpatterns = [
      path('', Index.as_view(), name="Index"),
]
