
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("", include("blog.urls")),
    # path("auth/", include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
