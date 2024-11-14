from django.contrib import admin
from django.urls import path,include
from HomeAPP import views as M
from DropDown import views as D
from.import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h/',M.home,name='home'),
    path('in/',M.signin,name='signin'),
    path('up/',M.signup,name='signup'),
    path('pass/',M.reset,name='reset'),
    path('projects/', M.project_list, name='project_list'),
    path('sign-in/', M.signin, name='sign_in'),
    path('profile/', M.profile, name='profile'),
    path('sign-up/', M.signup, name='sign_up'),
    path('upload/', M.Upload_project, name='upload'),
    path('new/',M.featureprojectlist, name='new'),
    path('edu/',D.education,name='education'),
    path('bus/',D.bussiness,name='bussiness'),
    path('medical/',D.medical,name='medical'),
    path('disaster/',D.disaster,name='disaster'),
    path('education/',D.education_info,name='educationInfo'),
    path('business/',D.bussiness_info,name='bussinessInfo'),
    path('medicall/',D.medical_info,name='medicalInfo'),
    path('disasters/',D.disaster_info,name='disasterInfo'),   
    path('<str:id>/',M.details,name='details'),
    path('update/<str:id>',M.update_project,name='update'),
    path('delete_p/<int:id>', M.delete_p, name="delete_p"),
    path('',M.Mamun,name='mamun'),
    # path('donate/', M.donate, name='donate'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
