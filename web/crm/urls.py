from django.urls import path

from .views import UsersListView

app_name = 'crm'

urlpatterns = [
    path('api/users/', UsersListView.as_view(), name='users'),

]
