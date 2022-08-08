from django.urls import path
from . import views
from .views import redirect_view

urlpatterns = [
    path('about',views.about,name='about'),
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('signin',views.signin,name='signin'),
    path('details',views.details,name='details'),
    path('validate',views.validate,name='validate'),
    path('worker',views.worker,name='worker'),
    path('owner',views.owner,name='owner'),
    path('worker_details',views.worker_details,name='worker_details'),
    path('owner_details',views.owner_details,name='owner_details'),
    path('skip_owner_details',views.skip_owner_details,name='skip_owner_details'),
    path('skip_worker_details',views.skip_worker_details,name='skip_worker_details'),
    path('general_owner_chef',views.general_owner_chef,name='general_owner_chef'),
    path('general_owner_electrician',views.general_owner_electrician,name='general_owner_electrician'),
    path('general_owner_singer',views.general_owner_singer,name='general_owner_singer'),
    path('general_owner_dancer',views.general_owner_dancer,name='general_owner_dancer'),
    path('general_owner_beautician',views.general_owner_beautician,name='general_owner_beautician'),
    path('general_worker_chef',views.general_worker_chef,name='general_worker_chef'),
    path('general_worker_electrician',views.general_worker_electrician,name='general_worker_electrician'),
    path('general_worker_singer',views.general_worker_singer,name='general_worker_singer'),
    path('general_worker_dancer',views.general_worker_dancer,name='general_worker_dancer'),
    path('general_worker_beautician',views.general_worker_beautician,name='general_worker_beautician'),
    path('general_worker_sales',views.general_worker_sales,name='general_worker_sales'),
    path('general_owner_sales',views.general_owner_sales,name='general_owner_sales'),
    path('feedback',views.feedback,name='feedback'),
    path('feedback_details',views.feedback_details,name='feedback_details'),

    path('feedback_results',views.feedback_results,name='feedback_results'),

    path('choose_feedback',views.choose_feedback,name='choose_feedback'),
]