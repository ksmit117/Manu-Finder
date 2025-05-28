"""
URL configuration for TechStartup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('Tsearch_manu/', views.Tsearch_manu, name='Tsearch_manu'),  # Manufacturer search page
    path('about/', views.about, name='about'),  # About page
    path('search/', views.search_view, name='search'),  # Search page
    path('manufacturer/<int:manufacturer_id>/', views.manufacturer_detail, name='manufacturer_detail'), # Manufacturer detail page
    path('login/', views.login_view, name='login'),  # Login page
    path('signup/', views.signup_view, name='signup'),  # Signup page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),  # Forgot password page
    path('manu/', views.Manu, name='manu'),  # PDE page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('settings/', views.settings_view, name='settings'),  # Settings page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('help/', views.help_view, name='help'),  # Help page
    path('test/', views.test, name='test'),  # Test page
    path('test_search/', views.test_search, name='test_search'),  # Test search page
    path('test_result/', views.test_result, name='test_result'),  # Test result page
    path('redacted/', views.redacted, name='redacted'),  # Redacted page
    path('z1/', views.z1, name='z1'),  # Z1 page
]
