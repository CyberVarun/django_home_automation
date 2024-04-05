from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('sensor/<int:state>', views.sensor, name='sensor'),
    path('toggleled/<int:led>/<int:state>', views.toggleled, name='toggleled')
]
