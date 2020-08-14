from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from backend import views



# router.register(r'users', views.UserViewSet)
# router.register(r'modules', views.ModulesViewSet)
# router.register(r'multiplayer', views.MultiplayerViewSet)
# router.register(r'dashboard', views.DashboardViewSet)
# router.register(r'profile', views.ProfileViewSet)
# router.register(r'tutors', views.TutorViewSet)
# need to hook router.urls to urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('modules/', views.modules, name='modules'),
    path('arithmetic/', views.arithmetic, name='arithmetic'),
    path('tutors/', views.tutors, name='tutors'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('multiplayer/', views.multiplayer, name='multiplayer'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('benchmark_test/', views.benchmark_test, name='benchmark_test'),
    path('practice_test/', views.practice_test, name='practice_test')

    # path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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