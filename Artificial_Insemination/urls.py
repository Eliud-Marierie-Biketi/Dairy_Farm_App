from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cattle_management/', include('cattle_management.urls')),
    path('artificial_insemination/', include('Artificial_Insemination.urls')),
]
