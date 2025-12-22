from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    if request.user.is_staff:  # админ
        return render(request, 'user/admin_profile.html')
    return render(request, 'user/user_profile.html')
