from django.urls import path, include

urlpatterns = [
  path('schools/', include('api.admin.school.urls')),
  path('classrooms/', include('api.admin.classroom.urls')),
  path('users/', include('api.admin.user.urls')),
  path('subjects/', include('api.admin.subject.urls')),
  path('tests/', include('api.admin.test.urls')),
  path('scores/', include('api.admin.score.urls')),
  path('notifications/', include('api.admin.notification.urls')),
]

