from django.shortcuts import *
from django.http import *
from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.models import Group


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    # students = Student.objects.all()
    # total_students = students.count()
    leased = Lease.objects.all()
    books_issued = leased.filter(status='issued').count()
    books_returned = leased.filter(status='returned').count()
    books = Book.objects.all()
    # teachers = Teacher.objects.all()
    # total_teachers = teachers.count()
    members = Member.objects.all()
    total_teachers = members.filter(teacher=True).count()
    total_students = members.filter(student=True).count()
    total_members = members.count()
    context = {'leased': leased,
               'books': books,
               'books_issued': books_issued,
               'books_returned': books_returned,
               'members': members,
               'total_teachers': total_teachers,
               'total_students': total_students,
               'total_members': total_members}
    return render(request, 'index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def book(request, book):
    books = Book.objects.get(id=book)
    # booksFilter = BookFilter(request.GET, queryset=books)
    # books = booksFilter.qs
    context = {'books': books}
               # 'booksFilter': booksFilter}
    return render(request, 'books.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def book0(request):
    books = Book.objects.all()
    booksFilter = BookFilter(request.GET, queryset=books)
    books = booksFilter.qs
    context = {'books': books,
               'booksFilter': booksFilter}
    return render(request, 'books0.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def member(request, member):
    member = Member.objects.get(id=member)
    leased = member.lease_set.all()
    books = Book.objects.all()
    books_issued = leased.filter(status='issued').count()
    leaseFilter = LeaseFilter(request.GET, queryset=leased)
    leased = leaseFilter.qs
    context = {'member': member,
               'leased': leased,
               'leaseFilter': leaseFilter,
               'books': books,
               'books_issued': books_issued}
    return render(request, 'members.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def member0(request):
    member = Member.objects.all()
    memberFilter = MemberFilter(request.GET, queryset=member)
    member = memberFilter.qs
    context = {'member': member,
               'memberFilter': memberFilter}
    return render(request, 'members0.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def report(request):
    # student = Student.objects.all()
    # total_students = student.count()
    # teacher = Teacher.objects.all()
    # total_teachers = teacher.count()
    member = Member.objects.all()
    total_members = member.count()
    leased = Lease.objects.all()
    books_issued = leased.filter(status='issued').count()
    books_returned = leased.filter(status='returned').count()
    context = {'member': member,
               'leased': leased,
               'total_members': total_members,
               'books_issued': books_issued,
               'books_returned': books_returned}
    return render(request, 'report.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createMember(request):
    form = MemberForm()
    if request.method == 'POST':
        # print('Printing post:', request.POST)
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'member_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'book_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createLease(request):
    form = LeaseForm()
    if request.method == 'POST':
        # print('Printing post:', request.POST)
        form = LeaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'Lease_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateLease(request, lease):
    leased = Lease.objects.get(id=lease)
    form = LeaseForm(instance=leased)
    if request.method == 'POST':
        form = LeaseForm(request.POST, instance=leased)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'lease_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateBook(request, updbook):
    books = Book.objects.get(id=updbook)
    form = BookForm(instance=books)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'book_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateMember(request, updmember):
    members = Member.objects.get(id=updmember)
    form = MemberForm(instance=members)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=members)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'member_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteLease(request, lease):
    leased = Lease.objects.get(id=lease)
    if request.method == 'POST':
        leased.delete()
        return redirect('/')
    context = {'items': leased}
    return render(request, 'delete_lease.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteMember(request, member):
    members = Member.objects.get(id=member)
    if request.method == 'POST':
        members.delete()
        return redirect('/')
    context = {'items': members}
    return render(request, 'delete_member.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteBook(request, book):
    books = Book.objects.get(id=book)
    if request.method == 'POST':
        books.delete()
        return redirect('/')
    context = {
        'items': books
    }
    return render(request, 'delete_book.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def Faq(request):
    context = {}
    return render(request, 'faq.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def Helpdesk(request):
    context = {}
    return render(request, 'helpdesk.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'member'])
def ProfilePageMember(request):
    member = request.user.member
    form = MemberForm0(instance=member)
    if request.method == 'POST':
        form = MemberForm0(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'member_profile.html', context)


@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'successfully created user: ' + username)
            return redirect('/login/')
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def UserPage(request):
    lease = request.user.member.lease_set.all()
    print(lease)
    context = {
        'lease': lease
    }
    return render(request, 'user-home.html', context)