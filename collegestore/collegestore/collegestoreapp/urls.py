from django.urls import path,include

from collegestoreapp import views
app_name='collegestoreapp'
urlpatterns = [
    path('',views.home,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('details/',views.details,name='details'),
    path('ajax/load_course/',views.load_course,name='ajax_load_course'),
    path('logout/',views.logout,name='logout'),
    path('wikisearch/<str:name>',views.wikisearch,name='wikisearch'),
    path('orderconfirm/',views.orderconfirm,name="orderconfirm")



]