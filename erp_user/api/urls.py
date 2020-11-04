from django.urls import path

from erp_user.api.views import UserRegisterView

app_name = 'api_erp_user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),
    # path('account/', account_settings, name="account"),
    # path('', user_page, name='user_page'),
]
