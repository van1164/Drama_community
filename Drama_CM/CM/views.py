from django.shortcuts import render
from .models import Account,DRAMA
# Create your views here.

def main(request):
    return render(request, 'main/main.html', {})


def verify(id,password):
    if Account.objects.filter(id=id).exists():
        n = Account.objects.get(id=id)
        result=dict()
        result['name'] = n.name
        result['drama'] = n.watched_drama
        return result
    else:
        return False
    

def index(request):
    data = {'login':False}
    if request.method =="POST":
        uid = request.POST.get("userid",None)
        pw = request.POST.get("password",None)
        print("---------------------")
        user_data = verify(uid,pw)
        data['name'] = user_data['name']
        data['drama'] = user_data['drama']
        print(data['name'])
        print("---------------------")
        data['login'] = True
    return render(request, 'main/index.html',data)

def login(request):
    return render(request, 'main/login.html',{})