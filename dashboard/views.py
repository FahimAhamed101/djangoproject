from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets
from .serializers import TransactionListSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import User,Transaction
def _usertrans_id(request):
    usertrans = request.session.session_key
    if not usertrans:
        usertrans = request.session.create()
    return usertrans

def index(request):
    return render(request, 'index.html')

def data_view(request):
    try:
        
        if request.user.is_authenticated:
            transaction = Transaction.objects.filter(user=request.user)
            user= User.objects.filter(user=request.user)
        else:
            userid = User.objects.get(usertrans_id=_usertrans_id(request))
            transaction = Transaction.objects.filter(user=userid)
        
        
    except ObjectDoesNotExist:
        pass #just ignore
    
    context = {
        
        'transaction': transaction,
         'userinfo': userinfo,
        
    }
    return render(request, 'data.html',context)
def register(request):
    
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = 'default/default-user.png'
            profile.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html')


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        return redirect('edit_profile')
        
    return render(request, 'login.html', {'form': form, 'msg': msg})

def logout(request):
    auth.logout(request)
    
    return redirect('login')

# Create your views here.
def dashboard(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'dashboard.html', {'form': form, 'msg': msg})


@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    print(userprofile)
    userprofileid = UserProfile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
         'userprofile': userprofile,
        'profile_form': profile_form,
        'userprofileid': userprofileid,
    }
    return render(request, 'Profile.html', context)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionListSerializer
    def get_queryset(self):
        
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
            queryset = Transaction.objects.filter(user=self.request.user).order_by("-created_at")
        else:
            permission_classes = [IsAuthenticated]
            queryset = Transaction.objects.filter(user=self.request.user).order_by("-created_at")
        return queryset
    
    
    
