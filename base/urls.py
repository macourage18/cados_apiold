from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)


urlpatterns = [
  path('', views.endpoints),

  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('advocates/', views.advocate_list, name="advocates"),
  # path('advocates/<str:username>/', views.advocate_details),
  path('advocates/<str:username>/', views.AdvocateDetial.as_view()),

  #companies
  path('companies/', views.companies_list),

  #compianies id
  path('companies/<str:name>/', views.companies_details)
]