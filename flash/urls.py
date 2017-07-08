
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
	url(r'^listing', views.listing, name='listing'),
	url(r'^jsonlisting', views.jsonlisting, name='jsonlisting'),
	url(r'^timingListing', views.timingListing, name='timingListing'),
	url(r'^iterlist', views.iterlist, name='iterlist'),
	url(r'^subsetq', views.subsetq, name='subsetq'),
	url(r'^postarg', views.postarg, name='postarg'),
	url(r'^postbout', views.postBout, name='postBout'),
	url(r'^topscores', views.topscores, name='topscores'),
	url(r'^selgrid', views.selgrid, name='selgrid'),
]

