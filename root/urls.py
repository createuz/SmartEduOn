from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.click import TestView
from home.views import Page404
from home.viewset import DidUserBuy
from rest_framework.authtoken import views
from simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from . import router

handler404 = Page404
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('backoffice/', include('backoffice.urls')),
    path('quizzes/', include('quiz.urls')),
    path('api1234/', include(router.router.urls)),
    path('api/did-user-buy/', DidUserBuy.as_view(), name="is-user-bought"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/paycom/', include('paycom.urls')),
    path('api/uniredpay/', include('uniredpay.urls')),
    path('click/transaction/', TestView.as_view()),

    # swagger
    path('swagger.json/', schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
