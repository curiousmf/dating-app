from django.shortcuts import render
from dating.models import Person

# Create your views here.
def show_profiles(request):
    context = {'profiles': Person.objects.all()}
    return render(request,
                  'index.html',
                  context=context)

def show_profile(request, profile_id):
    context = {'profile':Person.objects.get(pk = profile_id)}
    return render(request,
                  'profile.html',
                  context=context)

def show_registration_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        status = request.POST.get('status')
        salary = request.POST.get('salary')
        description = request.POST.get('description')

        Person.objects.create(name = name,
                              surname = surname,
                              age = age,
                              status = status,
                              salary = salary,
                              description = description)
        
    return render(request, 'registration.html')