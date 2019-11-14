# from django.urls import path

# from . import views

#  adding namespace to differenciate apps
# app_name = 'polls'

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PollView.as_view()),
    url(r'^(?P<poll_id>[0-9A-Za-z]+)/?$', views.EditPollView.as_view()),
]