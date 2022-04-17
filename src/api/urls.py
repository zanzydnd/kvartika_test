from django.urls import re_path, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from api.views import PostViewSet

router = routers.SimpleRouter()

router.register(r"post", PostViewSet, "simple")

schema_view = get_schema_view(
    openapi.Info(
        title="Referal API",
        default_version="v1",
        description="Hammer Systems",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="zanzydnd@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    re_path("swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

]

urlpatterns += router.urls