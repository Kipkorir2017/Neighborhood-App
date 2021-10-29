from django.conf.urls import  url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#create urls
urlpatterns = [
    url('',views.display_index,name='index'), 
    url('signup/', views.signup, name='signup'),
    url('search/', views.search, name='search'),
    url('profile/',views.profile, name='profile'),
    url('joinhood/<id>', views.join_hood, name='joinhood'),
    url('leavehood/<id>', views.leave_hood, name='leavehood'),
    url('update/<id>', views.update_profile, name='update_profile'),
    url('newhood/', views.hood, name='hood'),
    url('hood_info/(?P<id>\d+)', views.view_hood, name='view_hood'),
    url('new_post', views.new_post, name='post'),
    url('new_business/', views.new_business, name='new_business'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
