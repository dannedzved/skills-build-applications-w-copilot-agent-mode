
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
import os
from django.http import JsonResponse

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardEntryViewSet, basename='leaderboardentry')

# Custom API root to return the correct codespace URL
def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
    return JsonResponse({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'workouts': f'{base_url}/api/workouts/',
        'leaderboard': f'{base_url}/api/leaderboard/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api_root'),
    path('api/', include(router.urls)),
    path('', api_root, name='root'),
]
