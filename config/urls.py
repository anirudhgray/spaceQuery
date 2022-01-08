from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from apps.users.urls import router as user_router
from apps.saves.urls import router as save_router
from apps.externals.urls import router as external_router
from apps import users, externals

router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(save_router.registry)
router.registry.extend(external_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi/', get_schema_view(
        title="School Service",
        description="API developers hoping to use our service"
    ), name='openapi-schema'),
    path('api/v1/users/actions/', include(users.urls)),
    path('api/v1/externals/actions/', include(externals.urls))
]
