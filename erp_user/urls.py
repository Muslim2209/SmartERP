from django.urls import path

from erp_user.views import register_user, login_user, logout_user, user_page, account_settings

app_name = 'erp_user'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('account/', account_settings, name="account"),
    path('', user_page, name='user_page'),
]
