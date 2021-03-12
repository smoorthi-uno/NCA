from django.conf.urls import url
from . import views
from django.urls import path, re_path, include
from .views import nca, staff, volunteer
from nca.views import *

urlpatterns = [
    path('', nca.home, name='home'),

    path('Admins/', include(([
                                path('', nca.SignUpView.as_view(), name='signup'),
                                path('staffsignup/', staff.StaffSignUpView.as_view(), name='staff_signup'),
                                path('volunteersignup/', volunteer.VolunteerSignUpView.as_view(),
                                     name='volunteer_signup'),
                            ], 'nca'), namespace='admins')),

    path('Staff/', include(([
                                path('', staff.staff_home.as_view(), name='staff_home'),
                                path('activity_list', staff.activity_list, name='activity_list'),
                                path('activity/<int:pk>/detail/', staff.activity_detail, name='activity_detail'),
                                path('activity/<int:pk>/edit/', staff.activity_edit, name='activity_edit'),
                                path('activity/<int:pk>/delete/', staff.activity_delete, name='activity_delete'),
                                path('activity/new/', staff.activity_new, name='activity_new'),
                                path('activity/<int:pk>/notes/', staff.activity_notes, name='activity_notes'),
                            ], 'nca'), namespace='staff')),

    path('Volunteer/', include(([
                                    path('', volunteer.volunteer_home.as_view(), name='volunteer_home'),
                                ], 'nca'), namespace='volunteer')),


    # path('activity_list', views.activity_list, name='activity_list'),
    # path('activity/<int:pk>/detail/', views.activity_detail, name='activity_detail'),
    # path('activity/<int:pk>/edit/', views.activity_edit, name='activity_edit'),
    # path('activity/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    # path('activity/new/', views.activity_new, name='activity_new'),
    # path('activity/<int:pk>/notes/', views.activity_notes, name='activity_notes'),

]
