from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account has been created for {username}')
            return redirect("lol-login")
    else:
        form = UserRegisterForm()

    return render(request, "accounts/register.html", {'form': form})


@ login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(
                request, f'Account has been updated!')
            return redirect("lol-profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "accounts/profile.html", context)


class UserPostListView(ListView):
    model = Post
    template_name = 'accounts/profile.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
