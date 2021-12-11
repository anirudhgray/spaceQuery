from rest_framework import routers
from .views import HistoryViewSet, SaveViewSet


router = routers.SimpleRouter()
router.register("saves", viewset=SaveViewSet)
router.register("history", viewset=HistoryViewSet)

urlpatterns = [
]
