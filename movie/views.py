from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def Home(request):
    data = Movie.objects.all()
    d = {'data':data}
    return render(request,'carousel.html',d)

def Admin_Home(request):
    total_user=0
    total_movie=0
    total_booking=0
    for i in Customer.objects.all():
        total_user+=1
    for i in Movie.objects.all():
        total_movie+=1
    for i in Booking.objects.all():
        total_booking+=1
    d = {'total_user':total_user,'total_movie':total_movie,'total_booking':total_booking}
    return render(request,'admin_dash.html',d)

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if not user.is_staff:
            try:
                sign = Customer.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)
                error = "pat1"
            else:
                error = "not"
        elif user.is_staff:
            login(request,user)
            error="admin"
        else:
            error="not"
    d = {'error': error}
    return render(request, 'login.html', d)

def Signup_User(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        p = request.POST['pwd']
        d = request.POST['dob']
        ad = request.POST['add']
        e = request.POST['email']
        gen = request.POST['gen']
        i = request.FILES['img']
        con = request.POST['phone']
        lik = request.POST['like']
        user = User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)
        Customer.objects.create(user=user,gen=gen, dob=d, address=ad, contact=con, image=i, like=lik)
        error = True
    d = {'error': error}
    return render(request,'signup_user.html',d)

def Edit_Profile(request):
    error = False
    data = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        ad = request.POST['add']
        e = request.POST['email']
        try:
            i = request.FILES['img']
            data.image=i
            data.save()
        except:
            pass
        con = request.POST['phone']
        lik = request.POST['like']
        data.user.first_name = f
        data.user.last_name = l
        data.user.email = e
        data.user.save()
        data.address = ad
        data.contact = con
        data.like = lik
        data.save()
        error = True
    d = {'error': error,'data':data}
    return render(request,'edit_profile.html',d)

def Logout(request):
    logout(request)
    return redirect('home')

def Add_Certificate(request):
    if not request.user.is_staff:
        return redirect('login')
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        d = request.POST['des']
        Certificate.objects.create(
            name = n,
            description = d
        )
        error = True
    d = {'error': error}
    return render(request,'add_certificate.html',d)

def View_Certificate(request):
    if not request.user.is_staff:
        return redirect('login')
    data = Certificate.objects.all()
    d = {'data': data}
    return render(request,'view_certificate.html',d)

def Edit_Certificate(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Certificate.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        d = request.POST['des']
        data.name = n
        data.description = d
        data.save()
        error = True
    d = {'error': error,'data':data}
    return render(request,'edit_certificate.html',d)

def delete_certificate(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Certificate.objects.get(id=pid)
    data.delete()
    return redirect('view_certificate.html')

def Add_Movie_Type(request):
    if not request.user.is_staff:
        return redirect('login')
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        d = request.POST['des']
        Movie_Type.objects.create(
            name = n,
            description = d
        )
        error = True
    d = {'error': error}
    return render(request,'add_movie_type.html',d)

def View_Movie_Type(request):
    if not request.user.is_staff:
        return redirect('login')
    data = Movie_Type.objects.all()
    d = {'data': data}
    return render(request,'view_movie_type.html',d)

def Edit_Movie_Type(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Movie_Type.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        d = request.POST['des']
        data.name = n
        data.description = d
        data.save()
        error = True
    d = {'error': error,'data':data}
    return render(request,'edit_movie_type.html',d)

def delete_movie_type(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Movie_Type.objects.get(id=pid)
    data.delete()
    return redirect('view_movie_type.html')

def Add_Language(request):
    if not request.user.is_staff:
        return redirect('login')
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        d = request.POST['des']
        Language.objects.create(
            name = n,
            description = d
        )
        error = True
    d = {'error': error}
    return render(request,'add_language.html',d)

def View_Language(request):
    if not request.user.is_staff:
        return redirect('login')
    data = Language.objects.all()
    d = {'data': data}
    return render(request,'view_language.html',d)

def Edit_Language(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Language.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        d = request.POST['des']
        data.name = n
        data.description = d
        data.save()
        error = True
    d = {'error': error,'data':data}
    return render(request,'edit_language.html',d)

def delete_language(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Language.objects.get(id=pid)
    data.delete()
    return redirect('view_language.html')

def Add_Movie(request):
    if not request.user.is_staff:
        return redirect('login')
    error = False
    type1 = Movie_Type.objects.all()
    lan1 = Language.objects.all()
    cer1 = Certificate.objects.all()
    if request.method == 'POST':
        n = request.POST['name']
        l = request.POST['lang']
        t = request.POST['type']
        c = request.POST['certi']
        du = request.POST['dura']
        di = request.POST['dir']
        ca = request.POST['cast']
        r = request.POST['r_date']
        tr = request.POST['trailer']
        des = request.POST['des']
        img = request.FILES['image']
        lan = Language.objects.get(id=l)
        type = Movie_Type.objects.get(id=t)
        cer = Certificate.objects.get(id=c)
        Movie.objects.create(
            name = n,
            language = lan,
            type = type,
            certificate = cer,
            duration = du,
            director = di,
            casting = ca,
            release_date = r,
            trailer = tr,
            image = img,
            description = des
        )
        error = True
    d = {
        'error': error,
        'cert': cer1,
        'type': type1,
        'lang':lan1
    }
    return render(request,'add_movie.html',d)

def View_Movie(request):
    if not request.user.is_staff:
        return redirect('login')
    data = Movie.objects.all()
    d = {'data': data}
    return render(request,'view_movie.html',d)

def Edit_Movie(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Movie.objects.get(id=pid)
    error = False
    type1 = Movie_Type.objects.all()
    lan1 = Language.objects.all()
    cer1 = Certificate.objects.all()
    if request.method == "POST":
        n = request.POST['name']
        l = request.POST['lang']
        t = request.POST['type']
        c = request.POST['certi']
        du = request.POST['dura']
        di = request.POST['dir']
        ca = request.POST['cast']
        r = request.POST['r_date']
        if r:
            data.release_date = r
            data.save()
        else:
            pass
        try:
            img = request.FILES['image']
            data.image = img
            data.save()
        except:
            pass
        tr = request.POST['trailer']
        des = request.POST['des']
        lan = Language.objects.get(id=l)
        type = Movie_Type.objects.get(id=t)
        cer = Certificate.objects.get(id=c)
        data.name = n
        data.language = lan
        data.type = type
        data.certificate = cer
        data.duration = du
        data.director = di
        data.casting = ca
        data.trailer = tr
        data.description = des
        data.save()
        error = True
    d = {
        'error': error,
        'cert': cer1,
        'type': type1,
        'data': data,
        'lang': lan1
    }
    return render(request,'edit_movie.html',d)

def delete_movie(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = Movie.objects.get(id=pid)
    data.delete()
    return redirect('view_movie')

def Movie_detail(request,pid):
    data = Movie.objects.get(id=pid)
    time1 = Movie_Time.objects.all()
    if request.method=="POST":
        t = request.POST['time']
        d = request.POST['date']
        if request.user:
            data1 = Set_Timing.objects.create(
                time1=t,
                date1=d,
                movie=data
            )
        else:
            return redirect('home')
        return redirect('book_ticket',data1.id)
    d = {'data':data,'time1':time1}
    return render(request,'movie_detail.html',d)

def View_Trailer(request,pid):
    data = Movie.objects.get(id=pid)
    d = {'data':data}
    return render(request,'view_trailer.html',d)

def Book_Ticket(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Set_Timing.objects.get(id=pid)
    data1 = Booking.objects.filter(set_time=data)
    li = ""
    for i in data1:
        li+=","+i.seat
    error = False
    book=""
    if request.method=="POST":
        t = request.POST['name']
        n = request.POST['num']
        s = request.POST['seat']
        p = int(n)*120
        cust = Customer.objects.get(user=request.user)
        book = Booking.objects.create(user1=cust,user=t,set_time=data,ticket=n,price=p,seat=s)
        error=True
    d = {'data':data,'error':error,'li':li,'book':book}
    return render(request,'book_ticket.html',d)

def Movie_Payment(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data1 = Booking.objects.get(id=pid)
    error = False
    if request.method=="POST":
        try:
            t = request.POST['name']
            c = request.POST['card']
            c = request.POST['cvv']
            y = request.POST['date']
            data1.status = "Paid"
            data1.save()
            error = True
        except:
            data1.delete()
            return redirect('login')
    d = {'data':data1,'error':error}
    return render(request,'payment.html',d)

def View_Booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    cust = Customer.objects.get(user=user)
    data = Booking.objects.filter(user1=cust)
    d = {'data':data}
    return render(request,'view_booking.html',d)

def All_Movies(request,pid):
    language = ""
    if pid == 0:
        language = "ALL MOVIES"
        data = Movie.objects.all()
    if pid == 1:
        language = "Hindi Movies"
        lang = Language.objects.get(name="Hindi")
        data = Movie.objects.filter(language=lang)
    if pid == 2:
        language = "English Movies"
        lang = Language.objects.get(name="English")
        data = Movie.objects.filter(language=lang)
    if pid == 3:
        language = "South Movies"
        lang = Language.objects.get(name="South")
        data = Movie.objects.filter(language=lang)
    d = {'data': data,'language':language}
    return render(request,'all_movies.html',d)

def All_Booking(request):
    if not request.user.is_staff:
        return redirect('login')
    data = Booking.objects.all()
    d = {'data': data}
    return render(request,'all_booking.html',d)

def View_User(request):
    if not request.user.is_staff:
        return redirect('login')
    data = Customer.objects.all()
    d = {'data': data}
    return render(request,'view_user.html',d)

def delete_booking1(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Booking.objects.get(id=pid)
    data.delete()
    return redirect('all_booking')

def delete_booking(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Booking.objects.get(id=pid)
    data.delete()
    return redirect('view_booking')

def delete_user(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data = User.objects.get(id=pid)
    data.delete()
    return redirect('view_user')

def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'change_password.html',d)

