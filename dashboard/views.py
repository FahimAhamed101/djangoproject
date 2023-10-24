from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets
from .serializers import TransactionListSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.
from userauths.models import User
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


# Create your views here.
def dashboard(request):
    msg = None
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    
        #form = SignUpForm()
    return render(request,'dashboard.html',)




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
    
    
    
