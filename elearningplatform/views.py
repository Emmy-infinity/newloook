from django.shortcuts import redirect,render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login, logout,authenticate
from .forms import *

from .models import *
def home(request):
     videoobj=Videotutorial.objects.all()
     context={'videoobj':videoobj}
     return render(request,'caninstitutehome.html',context)
def quizz(request):
    question=Add_Questions.objects.all()
           
    paginator=Paginator(question,180)
    page = request.GET.get('page', 1)
    try:
          users = paginator.page(page)
    except PageNotAnInteger:
          users = paginator.page(1)
    except EmptyPage:
           users = paginator.page(paginator.num_page)
    if request.method == 'POST':
        
        score=0
        wrong=0
        correct=0
        total=0
        question_number=1
        for q in users:
            total+=1
            question_number+=1
            
            
            if q.Answer ==  request.POST.get(q.Question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        time=request.POST.get('timer')
        context = {
            'users':users,
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        time+=time
        
        return render(request,'results.html',context)
    else:
    
      
        
        
        
        return render(request,'multichoice.html',{'users': users})
 
def Notes(request):
    return(request,'cansinstitute.html')
def Videos(request):
    videoobj=Videotutorial.objects.all()
    context={'videoobj':videoobj}
    return(request,'caninstitutevideo.html',context)
def Register(request):
    return(request,'caninstitute.html')
def About(request):
    pass
def Article(request):
    
    articles=Articles2.objects.all()
    context={'articles':articles}
    return render(request,'caninstitutearticle.html',context)

def Learning_materials(request):
    return render(request,'multichoice.html')
def PrivacyPolicy(request):
    pass
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=createuserform()
        if request.method =='POST':
            form=createuserform(request.POST)
            if form.is_valid():
             user= form.save()
            return redirect('login')
        context={'form':form}
        return render(request,'register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'register.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')    


    
