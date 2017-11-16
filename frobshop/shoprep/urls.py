from django.conf.urls import url
from oscar.core.loading import get_class

app_name = 'shoprep'
home_view = get_class('promotions.views', 'HomeView')
urlpatterns = [
    url(r'^$', home_view.as_view(), name='index'),
]
