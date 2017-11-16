from django.conf.urls import url
from oscar.core.loading import get_class

app_name = 'shoprep'
catalogue_view = get_class('catalogue.views', 'CatalogueView')
urlpatterns = [
    url(r'^$', catalogue_view.as_view(), name='index'),
]
