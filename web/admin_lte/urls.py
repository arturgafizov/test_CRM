from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import TemplateAPIView

app_name = 'admin_lte'

router = DefaultRouter()

urlpatterns = [
    path('index/', TemplateAPIView.as_view(template_name='admin_lte/index.html'), name='index'),
    path('index2/', TemplateAPIView.as_view(template_name='admin_lte/index2.html'), name='index2'),
    path('index3/', TemplateAPIView.as_view(template_name='admin_lte/index3.html'), name='index3'),
    path('users/', TemplateAPIView.as_view(template_name='admin_lte/users.html'), name='users'),
]

urlpatterns += router.urls

"""Layout Options part"""
urlpatterns += [
    path('layout/top-nav/', TemplateAPIView.as_view(template_name='admin_lte/pages/layout/top-nav.html'),
         name='layout_top-nav'),
    path('layout/top-nav-sidebar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/top-nav-sidebar.html'),
         name='layout_top-nav-sidebar'),
    path('layout/boxed/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/boxed.html'), name='layout_boxed'),
    path('layout/fixed-sidebar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/fixed-sidebar.html'),
         name='layout_fixed-sidebar'),
    path('layout/fixed-navbar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/fixed-topnav.html'), name='layout_fixed-topnav'),
    path('layout/fixed-footer/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/fixed-footer.html'), name='layout_fixed-footer'),
    path('layout/collapsed-sidebar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/collapsed-sidebar.html'),
         name='layout_collapsed-sidebar')
]

"""Charts part"""
urlpatterns += [
    path('charts/chartjs/', TemplateAPIView.as_view(template_name='admin_lte/pages/charts/chartjs.html'),
         name='chartjs'),
    path('charts/flot/', TemplateAPIView.as_view(template_name='admin_lte/pages/charts/flot.html'), name='flot'),
    path('charts/inline/', TemplateAPIView.as_view(template_name='admin_lte/pages/charts/inline.html'), name='inline'),
]


"""Tables part"""
urlpatterns += [
    path('tables/jsgrid/', TemplateAPIView.as_view(template_name='admin_lte/pages/tables/jsgrid.html'),
         name='jsgrid_table'),
    path('tables/simple/', TemplateAPIView.as_view(template_name='admin_lte/pages/tables/simple.html'),
         name='simple_table'),
]


"""Pages part"""
urlpatterns += [
    path('pages/profile/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/profile.html'),
         name='pages_profile'),
]

"""Extra part"""
urlpatterns += [
    path('extra/login/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/login.html'),
         name='extra_login'),
    path('extra/register/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/register.html'),
         name='extra_register'),
    path('extra/forgot/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/forgot-password.html'),
         name='extra_forgot'),
    path('extra/recover/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/recover-password.html'),
         name='extra_recover'),

]
