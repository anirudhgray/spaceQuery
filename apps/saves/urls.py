from rest_framework import routers
from .views import SaveViewSet


router = routers.SimpleRouter()
router.register("saves", viewset=SaveViewSet)

urlpatterns = [
]
