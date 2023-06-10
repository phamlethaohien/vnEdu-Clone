from django.urls import path, include

urlpatterns = [
  path('users/', include('api.home.user.urls')),
  path('tests/', include('api.home.test.urls')),
  path('scores/', include('api.home.score.urls')),
]

