from django.shortcuts import render, get_object_or_404
from mainpage import models

# Create your views here.
def course_single(request, course_id):
    courses = get_object_or_404(models.course, pk=course_id)
    detail = models.detail.objects.first()
    facultie = models.facultie.objects.all()
    image = models.image.objects.first()

    for i in facultie:
        if i.name == courses.instructor:
            fac = i
            break


    context = {'courses': courses,
               'course_id': course_id,
               'detail': detail,
               'facultie': facultie,
               'image': image,
               'fac': fac,
               'course_single_page': 1,}

    return render(request, 'mainpage/course-single.html', context)