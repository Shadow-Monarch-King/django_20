from django.urls import path,include
from . import views
urlpatterns = [   
    path('login_view/',views.login_view, name = 'login_view'),
    path('account-view/',views.account_view, name = 'account_view'),
    path('logout-view/',views.logout_view, name = 'logout_view')
]
