
from django.conf.urls import url


from . import views
from .views import  user_delete,  user_detail, login, logout, user_update


urlpatterns = [

    # url(r'^user/(?P<slug>\w+)/$',views.displayuser.as_view(),name='candidate'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'apply',views.applyuser,name='apply'),
    url(r'update/<slug:slug>', views.user_update, name="edit-user-profile"),

    url('delete/(?P<slug>\w+)/$', views.user_delete, name='user_delete'),

]

