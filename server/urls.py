
from django.contrib import admin
from django.urls import path
import api.views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', api_views.store_data, name='store_data'),
    path('map/', api_views.map_data, name='map_data')
]
