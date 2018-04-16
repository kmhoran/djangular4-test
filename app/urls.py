from django.conf.urls import url
from app import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$', views.LinksPageView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)