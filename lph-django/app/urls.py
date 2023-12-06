from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import get_tables, salary_analysis, best_customers, delivery_summary, OrderViewSet, ReservationViewSet, EmployeeViewSet, ItemViewSet, PromotionViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'items', ItemViewSet, basename='item')
router.register(r'promotions', PromotionViewSet, basename='promotion')

urlpatterns = router.urls

urlpatterns = [
    # Your other URL patterns...
    path('get-tables/', get_tables, name='tables'),
    path('salary-analysis/', salary_analysis, name='salary_analysis'),
    path('best-customers/', best_customers, name='best_customers'),
    path('delivery-summary/', delivery_summary, name='delivery_summary'),
] + urlpatterns

