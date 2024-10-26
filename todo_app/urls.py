from django.urls import path
from .views import SignUpView, VerifyOTPView, SignInView, ToDoView

urlpatterns = [
    path('api/auth/signup/', SignUpView.as_view(), name='signup'),
    path('api/auth/verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('api/auth/signin/', SignInView.as_view(), name='signin'),
    path('api/todos/', ToDoView.as_view(), name='todos'),
]