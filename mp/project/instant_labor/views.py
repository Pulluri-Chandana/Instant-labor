from django.shortcuts import render

from django.http import HttpResponse
from .models import Credentials
from .models import Worker
from .models import Owner
from .models import Feedback
from django.shortcuts import redirect

#def hello(request)



def feedback(request):

    return render(request,'feedback.html')
   
def feedback_details(request):

    feed=request.GET['subject']

    rat=request.GET['rating']

    from_mail=request.GET['frname']

    to_mail=request.GET['toname']

    obj=Feedback(from_per_mail=from_mail,to_per_mail=to_mail,rating=rat,feed=feed)

    obj.save()

    para=to_mail

    query_set=Feedback.objects.filter(to_per_mail=para)

    return render(request,'feedback_result.html',{'feedbackList':query_set})

def feedback_results(request):

    query_set=Feedback.objects.all()

    return render(request,'feedback_result.html',{'feedbackList':query_set})

def choose_feedback(request):

    para=request.GET['email']

    query_set=Feedback.objects.filter(to_per_mail=para)

    return render(request,'feedback_result.html',{'feedbackList':query_set})

def feedback(request):

    return render(request,'feedback.html')

def feedback_details(request):

    feed=request.GET['subject']

    rat=request.GET['rating']

    from_mail=request.GET['frname']

    to_mail=request.GET['toname']

    obj=Feedback(from_per_mail=from_mail,to_per_mail=to_mail,rating=rat,feed=feed)

    obj.save()

    para=to_mail

    query_set=Feedback.objects.filter(to_per_mail=para)

    return render(request,'feedback_result.html',{'feedbackList':query_set})

def feedback_results(request):

    query_set=Feedback.objects.all()

    return render(request,'feedback_result.html',{'feedbackList':query_set})

def choose_feedback(request):

    para=request.GET['email']

    query_set=Feedback.objects.filter(to_per_mail=para)

    return render(request,'feedback_result.html',{'feedbackList':query_set})


def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'welcome.html')
def login(request):
    return render(request,'login.html')
def signin(request):
    return render(request,'signin.html')  
def worker(request):
    return render(request,'Worker.html')
def owner(request):
    return render(request,'owner.html')
def details(request):
    u=request.GET['name']
    p=request.GET['word']
    obj = Credentials(user=u,passw=p)
    obj.save()
    return  render(request,'firstpage.html')  
def skip_owner_details(request):
    query_set=Owner.objects.all()
    return render(request,'skip_owner.html',{'OwnerList':query_set})
def worker_details(request):
    fname=request.GET['fname']
    lname=request.GET['lname']
    skills=request.GET['skills']
    contact_no=request.GET['contact']
    email=request.GET['email']
    addr=request.GET['addr']
    obj=Worker(fname=fname,lname=lname,skills=skills,contact_no=contact_no,email=email,addr=addr)
    obj.save()
    query_set=Owner.objects.filter(skills_req__contains=skills)
    if(len(query_set)==0):
                        return render(request,'zero_matches_owner.html')
    return render(request,'worker_results.html',{'OwnerList':query_set})
def skip_worker_details(request):
    query_set=Worker.objects.all()
    return render(request,'skip_worker.html',{'workerList':query_set})
    
def owner_details(request):
    fname=request.GET['fname']
    lname=request.GET['lname']
    skills_req=request.GET['skills']
    contact_no=request.GET['contact']
    email=request.GET['email']
    addr=request.GET['addr']
    obj=Owner(fname=fname,lname=lname,skills_req=skills_req,contact_no=contact_no,email=email,addr=addr)
    obj.save()
    query_set=Worker.objects.filter(skills__contains=skills_req)
    if(len(query_set)==0):
                        return render(request,'zero_matches_worker.html')
    return render(request,'owner_results.html',{'workerList':query_set})
def general_owner_chef(request):
     general_skill="Chef"
     query_set=Owner.objects.filter(skills_req__contains=general_skill)
     return render(request,'worker_results.html',{'OwnerList':query_set}) 
def general_owner_singer(request):
     general_skill="Singing"
     query_set=Owner.objects.filter(skills_req__contains=general_skill)
     return render(request,'worker_results.html',{'OwnerList':query_set}) 
def general_owner_dancer(request):
     general_skill="Dancing"
     query_set=Owner.objects.filter(skills_req__contains=general_skill)
     return render(request,'worker_results.html',{'OwnerList':query_set}) 
def general_owner_beautician(request):
     general_skill="Beautician"
     query_set=Owner.objects.filter(skills_req__contains=general_skill)
     return render(request,'worker_results.html',{'OwnerList':query_set})  
def general_owner_electrician(request):
     general_skill="Electrician"
     query_set=Owner.objects.filter(skills_req__contains=general_skill)
     return render(request,'worker_results.html',{'OwnerList':query_set}) 
def general_owner_sales(request):
     general_skill="Sales men"
     query_set=Owner.objects.filter(skills_req__contains=general_skill)
     return render(request,'worker_results.html',{'OwnerList':query_set}) 
def general_worker_chef(request):
        general_skill="Chef"
        query_set=Worker.objects.filter(skills__contains=general_skill)
        return render(request,'owner_results.html',{'workerList':query_set})
def general_worker_singer(request):
        general_skill="Singing"
        query_set=Worker.objects.filter(skills__contains=general_skill)
        return render(request,'owner_results.html',{'workerList':query_set})
def general_worker_dancer(request):
        general_skill="Dancing"
        query_set=Worker.objects.filter(skills__contains=general_skill)
        return render(request,'owner_results.html',{'workerList':query_set})
def general_worker_beautician(request):
        general_skill="Beautician"
        query_set=Worker.objects.filter(skills__contains=general_skill)
        return render(request,'owner_results.html',{'workerList':query_set})
def general_worker_electrician(request):
        general_skill="Electrician"
        query_set=Worker.objects.filter(skills__contains=general_skill)
        return render(request,'owner_results.html',{'workerList':query_set})
def general_worker_sales(request):
        general_skill="Sales men"
        query_set=Worker.objects.filter(skills__contains=general_skill)
        return render(request,'owner_results.html',{'workerList':query_set})
def validate(request):
    u=request.GET['name']
    p=request.GET['word']
    user_name=Credentials.objects.filter(user=u,passw=p).values('user')[:1]

    worker_details_name=Worker.objects.filter(email=user_name).values('skills')
    if(len(worker_details_name)>0):
                  query_set=Owner.objects.filter(skills_req__contains=worker_details_name)
                  if(len(query_set)==0):
                        return render(request,'zero_matches_worker.html')
                  return render(request,'worker_results.html',{'OwnerList':query_set}) 
    owner_details_name=Owner.objects.filter(email=user_name).values('skills_req')
    if(len(owner_details_name)>0):
        query_set=Worker.objects.filter(skills__contains=owner_details_name)
        print(len(query_set))
        if(len(query_set)==0):
                  return render(request,'zero_matches_owner.html')
        else:
                  return render(request,'owner_results.html',{'workerList':query_set})
    if len(user_name)>0:
        
        return render(request,'firstpage.html')
    else:
        return render(request,'error.html')

