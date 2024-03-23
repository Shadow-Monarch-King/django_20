from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as log_in
# Create your views here.
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



def account_view(request):
    
    session_name = request.user.username
    session_key = request.session.session_key
    print("Session NAme : ",session_name)
    print("Session NAme : ",session_key)
    context = {
        'session_name': session_name,
        'session_key'  :session_key
    }
    return render(request,'accounts/view.html',context)



