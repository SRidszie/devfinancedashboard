
from django.urls import path
from Finance_system import views
urlpatterns = [
    path('save-example/', views.save_example, name="save_example"),
]