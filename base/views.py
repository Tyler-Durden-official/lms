from base.forms import IssueBookForm
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from .forms import IssueBookForm
from django.contrib.auth import authenticate, login, logout
from . import forms, models
from datetime import date
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

@login_required(login_url = '/admin_login')
def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        book_id = request.POST['book_id']
        books = Book.objects.filter(book_id=book_id)
        if books:
            return HttpResponse("Enter unique book id and try again")
        category = request.POST['category']
        availability = request.POST['availability']
        books = Book.objects.create(name=name, author=author, book_id=book_id, category=category, availability=availability)
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")

@login_required(login_url = '/admin_login')
def view_books_admin(request):
    books = Book.objects.all()
    return render(request, "view_books_admin.html", {'books':books})

@login_required(login_url = '/student_login')
def view_books_student(request):
    books = Book.objects.all()
    return render(request, "view_books_student.html", {'books':books})

@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html", {'students':students})

@login_required(login_url = '/admin_login')
def issue_book(request):
    form = forms.IssueBookForm()
    if request.method == "POST":
        form = forms.IssueBookForm(request.POST)
        book_id = request.POST['book_id2']
        if form.is_valid():
            obj = models.IssuedBook()
            obj.student_id = request.POST['name2']
            obj.book_id = book_id
            obj.save()
            book = models.Book.objects.filter(book_id=book_id).first()
            book.availability -= 1
            book.save()
            alert = True
            return render(request, "issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issue_book.html", {'form':form})

@login_required(login_url = '/admin_login')
def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(book_id=i.book_id))
        students = list(models.Student.objects.filter(user=i.student_id))
        count=0
        for l in books:
            t=(i.id,students[count].user,students[count].user_id,books[count].name,books[count].book_id,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            count+=1
            details.append(t)
    return render(request, "view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})

@login_required(login_url = '/student_login')
def student_issued_books(request):
    student = Student.objects.filter(user_id=request.user.id).first()
    issuedBooks = IssuedBook.objects.filter(student_id=student.user_id)
    li1 = []
    li2 = []

    for i in issuedBooks:
        books = Book.objects.filter(book_id=i.book_id)
        for book in books:
            days=(date.today()-i.issued_date)
            d=days.days
            fine=0
            if d>15:
                day=d-14
                fine=day*5
            t=(book.name, book.author, issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
            li1.append(t)
    return render(request,'student_issued_books.html',{'li1':li1})

@login_required(login_url = '/student_login')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url = '/student_login')
def edit_profile(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        roll_no = request.POST['roll_no']
        image = request.POST['image']
        student.user.email = email
        student.phone = phone
        student.branch = branch
        student.roll_no = roll_no
        student.image = image
        student.user.save()
        student.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

def delete_book(request, myid):
    books = Book.objects.filter(id=myid).first()
    issued_books = IssuedBook.objects.filter(book_id=books.book_id)
    if issued_books:
        return HttpResponse("Error: The issued books are not returned by students yet. Try again after retrieving them.")
    books.delete()
    return redirect("/view_books_admin")

def delete_request(request, myid):
    request_book = RequestBook.objects.filter(id=myid)
    request_book.delete()
    return redirect("/view_requested_book")

def accept_request(request, myid):
    request_book = RequestBook.objects.filter(id=myid).first()
    request_book.status = "Accepted"
    request_book.save()
    return redirect("/view_requested_book")

def reject_request(request, myid):
    request_book = RequestBook.objects.filter(id=myid).first()
    request_book.status = "Rejected"
    request_book.save()
    return redirect("/view_requested_book")

def cancel_request(request, myid):
    request_book = RequestBook.objects.filter(id=myid).first()
    request_book.delete()
    return redirect("/student_requested_books")

def student_track_request(request, myid):
    return render(request, "student_track_request.html", {'id' : myid})

def admin_track_request(request, myid):
    return render(request, "admin_track_request.html",{'id':myid})

def delete_student(request, myid):
    students = Student.objects.filter(id=myid)
    student_name = students.first().user
    issued_books = IssuedBook.objects.filter(student_id=myid)
    if issued_books:
        return HttpResponse("Error: The student has one or more issued books to be returned. Try again after retrieving them.")
    students.delete()
    u = User.objects.get(username=student_name)
    u.delete()
    return redirect("/view_students")

def delete_issue(request, myid):
    book_issued = IssuedBook.objects.filter(id=myid).first()
    book = Book.objects.filter(book_id=book_issued.book_id).first()
    book.availability += 1
    book.save()
    book_issued.delete()
    return redirect("/view_issued_book")

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html")

def dashboard(request):
    return render(request, "admin_home.html")

def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        roll_no = request.POST['roll_no']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Student.objects.create(user=user, phone=phone, branch=branch, roll_no=roll_no, image=image)
        user.save()
        student.save()
        alert = True
        return render(request, "student_registration.html", {'alert':alert})
    return render(request, "student_registration.html")

def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/profile")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/admin_home")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

def Logout(request):
    logout(request)
    return redirect ("/")

def request_book(request):
    form = forms.RequestBookForm()
    if request.method == "POST":
        form = forms.RequestBookForm(request.POST)
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        reason = request.POST['reason']
        if form.is_valid():
            obj = models.RequestBook()
            student = models.Student.objects.filter(user_id = request.user.id).first()
            obj.student_id = student.id
            obj.book_name = book_name
            obj.author_name = author_name
            obj.reason = reason
            obj.student_dept = student.branch
            obj.save()
            alert = True
            return render(request, "request_book.html", {'obj':obj, 'alert':alert})
    return render(request, "request_book.html", {'form':form})

@login_required(login_url = '/student_login')
def student_requested_books(request):
    student = Student.objects.filter(user_id=request.user.id).first()
    requestedBooks = RequestBook.objects.filter(student_id=student.id)
    li1 = []
    for i in requestedBooks:
        delete_button = False
        if i.status == "Rejected":
            delete_button = True
        t=(i.id,i.book_name, i.author_name, i.status, delete_button)
        li1.append(t)
    return render(request,'student_requested_books.html',{'li1':li1})

@login_required(login_url = '/admin_login')
def view_requested_book(request):
    requestedBooks = RequestBook.objects.all()
    details = []
    students = set()
    for i in requestedBooks:
        students.add(Student.objects.filter(id=i.student_id).first())
    for i in students:
        books = RequestBook.objects.filter(student_id=i.id)
        count = 0
        for l in books:
            t=(i.user,i.id,i.branch,books[count].book_name,books[count].author_name,books[count].date_of_request,books[count].status,books[count].id)
            count += 1
            details.append(t)
    return render(request, "view_requested_book.html", {'requestedBooks':requestedBooks, 'details':details})

@login_required(login_url = '/admin_login')
def permission_manager(request):
    requested_books = RequestBook.objects.filter(status = "Pending")
    return render(request, "permission_manager.html", {"books":requested_books})

def email_function():
    pass

def send_email(request, branch):
    requested_books = RequestBook.objects.filter(status = "Pending", student_dept = branch)
    for book in requested_books:
        branch = book.student_dept
        email = HoD.objects.filter(branch=branch).first()
        email_function()
    return redirect("/permission_manager")

@login_required(login_url = '/admin_login')
def view_hods(request):
    hods = HoD.objects.all()
    return render(request, "view_hods.html", {'hods':hods})

@login_required(login_url = '/admin_login')
def add_hod(request):
    if request.method == "POST":
        name = request.POST['name']
        branch = request.POST['branch']
        email = request.POST['email']
        hod = HoD.objects.create(name=name, email=email, branch=branch)
        hod.save()
        alert = True
        return render(request, "view_hods.html")
    return render(request, "view_hods.html")

@login_required(login_url = '/admin_login')
def edit_hod(request, myid):
    hod = HoD.objects.get(id=myid)
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        hod.email = email
        hod.name = name
        hod.save()
        alert = True
        return render(request, "view_hods.html")
    return render(request, "view_hods.html")