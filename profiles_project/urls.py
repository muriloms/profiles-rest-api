from django.contrib import admin
from django.urls import path, include


from profiles_api import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.UserLoginApiView.as_view()),
    path('api/', include('profiles_api.urls')),
]
