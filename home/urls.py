from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),
    url(r'^employee$', views.employeeApi),
    url(r'employee/([0-9]+)$', views.employeeApi),
    url(r'^get_all_employes_of_department/([0-9]+)$',
        views.get_all_employes_of_department),
    url(r'^employee/savefile', views.SaveFile)
    # path('', views.index, name='home'),
    # path('about', views.about, name='about'),
    # path('services', views.services, name='services')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
