"""lol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from accounts import views as accounts_views
from posts import views as posts_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from posts.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('register/', accounts_views.register, name="lol-signup"),
    path('profile/', accounts_views.profile, name="lol-profile"),
    path('blog/', PostListView.as_view(), name="lol-blog"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('profile/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="lol-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="entry/index.html"),
         name="lol-logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name="password_reset_complete"),
    path('', include('entry.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
