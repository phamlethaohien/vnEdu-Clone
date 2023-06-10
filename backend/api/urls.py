from django.urls import include, path

urlpatterns = [
    path('admin/', include('api.admin.urls')),
    path('home/', include('api.home.urls')),
    path('auth/', include('api.auth.urls')),
]
