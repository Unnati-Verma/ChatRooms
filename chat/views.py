from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'chatroom.html',{
        'room_name' : room_name
    })  

    #room_name is coming from the urls.py which passes the function then we return to template and pass it to the template