"""BlogRealTimeProject11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from BlogApp import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),


    path('post/', views.post_view),
    path('mail/', views.mail_send_view),
    path('signup/', views.Signup_view),
    path('postform/', views.post_form),
    path('postsucc/', views.postsuccview, name ='postsucc'),
    path('succ/', views.succview, name ='succ'),

    #path('<pk>/delete/',views.commentdelview.as_view(), name= 'delete1' ),
    path('<pk>/delete1/', views.postdeleteview.as_view(), name='delete'),
    path('update/<pk>', views.postupdateview.as_view(), name ='update'),




    path('tag/(P<tag_slug>[-\w]+)/', views.post_list_view, name='post_list_by_tag_name'),
    path('(P<year>\d{4})/(P<month>\d{2})/(P<day>\d{2})/(P<post>[-\w]+)/', views.post_detail_view, name='post_detail'),
    path("<id>/share/", views.mail_send_view),


    path("bssample/", views.bs_smaple_view),
    path('logout/', views.logout),
    path('post_list/', views.post_list_view),
    path('thankyou/', views.thankyou),

    path('tag/', views.post_list_view, name='post_list_by_tag_name'),
    re_path('^.*$', views.homepage),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

