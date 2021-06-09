from django.db.models.fields import DateTimeField
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from . import models
from . import forms


# Create your views here.
def index(request):
    detail = models.detail.objects.first()
    course = models.course.objects.all()
    facultie = models.facultie.objects.all()
    index_form = forms.RequestCallForm()
    image = models.image.objects.first()
    students_review = models.students_review.objects.all()
    context = {'detail': detail,
               'course': course,
               'facultie': facultie,
               'image': image,
               'students_review': students_review,
               'index_page': 1 }


    if request.method == 'POST':
        index_form = forms.RequestCallForm(request.POST)
        if index_form.is_valid():
            context['successfull'] = "Thanks For Contacting Us We Will Reply ASAP."
            first_name = index_form.cleaned_data['first_name']
            last_name = index_form.cleaned_data['last_name']
            city = index_form.cleaned_data['city']
            phone = index_form.cleaned_data['phone']
            message = index_form.cleaned_data['message']
            re = models.People_Request_For_Call(first_name=first_name, last_name=last_name, city=city, phone=phone, message=message, time_of_creation=datetime.datetime.now())
            re.save()
            return HttpResponseRedirect('/index/')
        else:
            context["unsuccessfull"] = "Please Try Again With Valid Entries."

    else:
        index_form = forms.RequestCallForm()
            
    context['index_form'] = index_form

    return render(request, "mainpage/index.html", context)

def all_course(request):
    course = models.course.objects.all()
    context = {'course': course, 
               'course_page': 1}

    return render(request, "mainpage/courses.html", context)


def contact(request):
    detail = models.detail.objects.first()
    form = forms.ContactUsForm()
    context = {'contact': contact, 
               'form': form, 
               'detail': detail,
               'contact_page': 1}
    
    ### Contact Us Form Code
    if request.method == 'POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            context['successfull'] = "Thanks For Contacting Us We Will Reply ASAP."
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            p = models.PeolpeContactUs(name=your_name, email=your_email, subject=subject, message=message, time_of_creation=datetime.datetime.now())
            p.save()
            return HttpResponseRedirect('/contact/')
        else:
            context["unsuccessfull"] = "Please Try Again With Valid Entries."

    else:
        form = forms.ContactUsForm()
            
    

    return render(request, "mainpage/contact.html", context)

    
def aboutus(request):
    image = models.image.objects.first()
    students_review = models.students_review.objects.all()
    detail = models.detail.objects.first()
    course = models.course.objects.all()
    about = models.AboutUs.objects.first()
    facultie = models.facultie.objects.all()

    context = {'detail': detail,
               'course': course,
               'image': image,
               'students_review': students_review,
               'about':about,
               'facultie': facultie,
               'about_page': 1 }

    return render(request, 'mainpage/about.html', context)
