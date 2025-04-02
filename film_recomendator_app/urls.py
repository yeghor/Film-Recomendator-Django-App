from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('query_results', views.query_result, name="query_results"),
    path('search_history', views.search_history, name="search_history"),
    path('delete_history', views.delete_history, name="delete_history"),
    path('top_searches', views.top_searches, name='top_searches')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
