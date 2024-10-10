from rest_framework import routers
from teste.viewsets import ProductViewSet, ClienteViewSet, EmployeeViewSet, SaleViewSet

router = routers.DefaultRouter()

router.register('products', ProductViewSet)
router.register('clients', ClienteViewSet)
router.register('employees', EmployeeViewSet)
router.register('sales', SaleViewSet)
urlpatterns = router.urls