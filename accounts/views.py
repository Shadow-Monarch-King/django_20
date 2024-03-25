from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as log_in, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login_view')
    context ={'form':form}
    return render(request,'accounts/register.html',context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        print(username,password)
        user = authenticate(request,username = username,password = password)
        if user is None:
            context = {'error':'Invalid Credetails'}
            return render(request,'accounts/login.html',context)
        else:
            log_in(request,user)
            session_name = request.user.username
            session_key = request.session.session_key
            print("Session NAme : ",session_name)
            print("Session NAme : ",session_key)
            return redirect('account_view')
        # log_in(request,user)
    return render(request,'accounts/login.html',context)


@login_required
def account_view(request):
    
    session_name = request.user.username
    session_key = request.session.session_key
    # session_expire = request.session.expire_date
    print("Session NAme : ",session_name)
    print("Session NAme : ",session_key)
    context = {
        'session_name': session_name,
        'session_key'  :session_key,
        # 'session_expire': session_expire
    }
    return render(request,'accounts/view.html',context)



def logout_view(request):   
    print(request)
    logout(request)
    return redirect('login_view')
    # render(request,'accounts/view.html',{})
    