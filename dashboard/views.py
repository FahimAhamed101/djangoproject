from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets
from .serializers import TransactionListSerializer
# Create your views here.
from .models import User,Userinfo,Transaction
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
            userinfo = Userinfo.objects.filter(user=request.user)
        else:
            userinfoid = Userinfo.objects.get(usertrans_id=_usertrans_id(request))
            transaction = Transaction.objects.filter(userinfoid=userinfoid)
        
        
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
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
           
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


# Create your views here.
def dashboard(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'dashboard.html', {'form': form, 'msg': msg})


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
    
    
    
