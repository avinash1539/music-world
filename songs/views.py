from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Case, When
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from songs.models import Songs, Watchlater, History


def home(request):
    s = Songs.objects.all()
    if request.user.is_authenticated:
        username1 = User.objects.get(username=request.user)
        return render(request, 'index.html', {'s': s, 'change': 'change', 'username1': username1})
    else:
        return render(request,'index.html',{'s':s})


#usersignup function
def signup(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['repeatpassword']
        if password == retype_password:
            try:
                user = User.objects.get(username=user_name)
                return render(request,'accounts/usersignup.html',{'message':'User Already Exist'})
            except Exception:
                newuser = User.objects.create_user(username=user_name,password=password,email=email)
                newuser.save()
                auth.login(request,newuser)
                username1 = User.objects.get(username=request.user)
                return redirect('home')

        else:
            return render(request,'accounts/usersignup.html',{'message':'password dont matched'})
    else:
        return render(request,'accounts/usersignup.html')

# create function for login
def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request, user)
            s = Songs.objects.all()
            username1 = User.objects.get(username=request.user)
            return redirect('home')
        else:
            return render(request,'accounts/userlogin.html',{'message':'invalid credential'})
    else:
        return render(request,'accounts/userlogin.html')


# fuction for logout
def logout(request):
    auth.logout(request)
    return redirect('home')

#function for play the song

def playsong(request,id):
    song = Songs.objects.get(song_id = id)
    if request.user.is_authenticated:
        username1 = User.objects.get(username=request.user)
        return render(request, 'playsong.html', {'song': song, 'change': 'change', 'username1': username1})
    else:
        return render(request, 'playsong.html', {'song': song})



def search(request):
    search_element = request.GET['search']
    print(search_element)
    allsong = Songs.objects.filter(Q(song_name__icontains=search_element) |
                                   (Q(singer_name__istartswith=search_element))
                                   )
    print(allsong)
    if allsong:
        if request.user.is_authenticated:
            username1 = User.objects.get(username=request.user)
            return render(request, 'search.html', {'song': allsong, 'change': 'change', 'username1': username1})
        else:
            return render(request, 'search.html', {'song': allsong})
    else:
        if request.user.is_authenticated:
            username1 = User.objects.get(username=request.user)
            message = "No Record Found"
            return render(request, 'search.html', {'message':message,'change': 'change', 'username1': username1})
        else:
            message = "No Record Found"
            return render(request, 'search.html', {'message':message})


#Function for add to watch later
def watchlater(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        song = Songs.objects.filter(song_id=song_id).first()
        if request.user.is_authenticated:
            username1 = User.objects.get(username=request.user)
            watch = Watchlater.objects.filter(user=request.user)
            for i in watch:
                if song_id == i.song_id:
                    messages.success(request, 'Your Song Is Already Added')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                watchlater = Watchlater(user=request.user, song_id=song_id)
                watchlater.save()
                messages.success(request, 'Congrats ! Song Is Successfully Addded')
            return render(request, f"playsong.html",{'song': song, 'change': 'change', 'username1': username1})
        else:
            messages.success(request, 'You Are Not Login....')

            return render(request, 'playsong.html', {"song": song})


    else:
        if request.user.is_authenticated:
            username1 = User.objects.get(username = request.user)
            wl = Watchlater.objects.filter(user=request.user)
            ids = []
            for i in wl:
                ids.append(i.song_id)

            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
            song = Songs.objects.filter(song_id__in=ids).order_by(preserved)
            return render(request, 'watchlater.html', {'song': song, 'change': 'change', 'username1': username1})


# function for History
def history(request):
    if request.method == 'POST':
        user = request.user
        song_id = request.POST['song_id']
        history = History(user=user, song_id=song_id)
        history.save()
        return redirect(f"/history/{song_id}")
    history = History.objects.filter(user=request.user)
    username1 = User.objects.get(username=request.user)
    ids = []
    for i in history:
        ids.append(i.song_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Songs.objects.filter(song_id__in=ids).order_by(preserved)
    return render(request, 'history.html', {'song': song, 'change': 'change', 'username1': username1})

# function for remove watchlater songs
def removewl(request,song_id):
    remove_element = Watchlater.objects.filter(user = request.user,song_id = song_id)
    remove_element.delete()
    return redirect('watchlater')

def removehs(request):
    remove_element = History.objects.filter(user=request.user)
    remove_element.delete()
    return redirect('history')

