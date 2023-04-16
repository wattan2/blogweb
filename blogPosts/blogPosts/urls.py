from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserAuth.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
