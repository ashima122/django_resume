from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from dashboard.models import *
from authentication.models import User
import pdfkit
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

class Vieww(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user.username
        print(user)
        try:
            profile = Profile.objects.get(user= request.user)

            print(profile.user)
            return render(request, 'main.html', {'user':user,'profile':profile.user })
        except:
            return render(request, 'main.html', {'user': user})
class EditResume(LoginRequiredMixin,View):
    def get(self, request):
        get_user = request.user
        print(get_user)
        profile = Profile.objects.get(user=get_user)
        return render(request, 'editresume.html',{"profile":profile})
    def post(self,request):
        profile =Profile.objects.get(user=request.user)
        profile.city=request.POST['city']
        profile.state=request.POST['state']
        profile.zipcode = request.POST['zipcode']
        profile.degree = request.POST['degree']
        profile.school = request.POST['school']
        profile.graduation = request.POST['graduation']
        profile.company = request.POST['company']
        profile.position = request.POST['position']
        profile.start_date = request.POST['start_date']
        profile.end_date = request.POST['end_date']
        profile.description = request.POST['description']
        profile.save()
        messages.success(request, 'Resume updated Successfully')
        return redirect('/')


class MainView(LoginRequiredMixin,View):
    def get(self, request):
        get_user = request.user.id
        print(get_user)
        user = User.objects.get(id=get_user)
        return render(request, 'dashboard.html', {"user": user})
    def post(self,request):
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        degree = request.POST['degree']
        school = request.POST['school']
        graduation = request.POST['graduation']
        company = request.POST['company']
        position = request.POST['position']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        description = request.POST['description']
        get_user = request.user.id
        user = User.objects.get(id=get_user)
        Profile.objects.create(user=user,city=city,state=state,zipcode=zipcode,degree=degree,school=school,graduation=graduation,company=company,position=position,start_date=start_date,end_date=end_date,description=description)
        messages.success(request, 'Resume created Successfully')
        return redirect('/')

class GetPdf(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        get_user = request.user.id
        print(get_user)
        user = User.objects.get(id=get_user)
        pro = Profile.objects.get(user=user)
        context = {'user': user, "pro": pro}
        html_string = render_to_string('pdf.html', context)
        # Convert HTML to PDF using pdfkit
        pdf_file = pdfkit.from_string(html_string, False)
        # Set the response content type
        response = HttpResponse(pdf_file, content_type='application/pdf')
        # Set the filename for the PDF download
        response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
        return response

@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    messages.success(request, 'User logout Successfully')
    return redirect('/login')


