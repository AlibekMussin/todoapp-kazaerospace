from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/cardlist/', include('todoapp.apps.cardlist.urls')),
    path('api/v1/user/', include('todoapp.apps.user.urls')),
]