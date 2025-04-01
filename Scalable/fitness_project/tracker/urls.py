from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home),
    path('login/', views.login_page),
    path('register/', views.register_page),
    path('dashboard/', views.dashboard),
    path('bmi/', views.bmi_page),
    path('activity-log/', views.log_activity_page),
    path('progress-chart/', views.progress_chart),

    # APIs
    path('api/register/', views.register_user),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/bmi/', views.calculate_bmi),
    path('api/tracker/log/', views.log_activity),
    path('api/tracker/progress/', views.get_progress),
]

