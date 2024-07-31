
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from journal.views import HomeView, AboutView, PublicationDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail')

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)