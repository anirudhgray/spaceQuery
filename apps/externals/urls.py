from rest_framework import routers
from .views import ExternalViewSet


router = routers.SimpleRouter()
router.register("externals", viewset=ExternalViewSet)

urlpatterns = [
]
