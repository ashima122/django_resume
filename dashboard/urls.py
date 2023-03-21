from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', Vieww.as_view()),
    path('resume', MainView.as_view()),
    path('edit-resume', EditResume.as_view()),
    path('get', GetPdf.as_view()),
    path("logout",logout_user),
]