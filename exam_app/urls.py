from django.urls import path
from . import views


app_name = 'exam'
urlpatterns = [
    path('',views.index,name='index'),
    path('reg&login',views.registeration_and_login,name='reg&login'),
    path('createUser',views.create_user),
    path('loginUser',views.login_user),
    path('logout',views.logout),
    path('dashboard',views.main_page,name='main_page'),
    path('trips/new',views.new_trip),
    path('trips/create',views.create_trip),
    path('trips/<int:tripID>',views.show_trip),
    path('trips/edit/<int:tripID>',views.edit_trip),
    path('trips/delete/<int:tripID>',views.delete_trip),
    path('trips/update/<int:tripID>',views.update_trip),
    path('trips/mytrip',views.show_mytrip),
    path('trips/cancel/<int:tripID>',views.cancel_trip),
    path('trips/join/<int:tripID>',views.join_trip), 
     
]    