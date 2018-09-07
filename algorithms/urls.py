from django.urls import path
from . import views


app_name = 'algorithms'
urlpatterns = [
	path('',views.index , name ='index'),
	path('eucledian',views.eucledianView,name='eucledian'),
	path('list',views.listView,name='list-all'),
	path('extended-eucledian',views.extended_eucledianView,name='extended_eucledian'),
	path('m-inverse-modular',views.m_inverseView,name='m_inverse')
]
