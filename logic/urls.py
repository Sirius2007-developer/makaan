from django.urls import path
from .views import a404, about, agent, testimonial, type, contact, list, index, aboutdetailview,\
    categdetailview, listdetailview, teamdetailview, teamUpdateView, teamDeleteView,\
    TeamCreateView, listUpdateView, listDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('404/', a404, name='a404'),
    path('about/', about, name='about'),
    path('agent/', agent, name='agent'),
    path('team/create/', TeamCreateView.as_view(), name="teamCreate"),
    path('testimonial/', testimonial, name='testimonial'),
    path('type/', type, name='type'),
    path('contact/', contact, name='contact'),
    path('list/', list, name='list'),
    path('aboutdetail/', aboutdetailview, name='aboutdetail'),
    path('categorydetail/<int:id>/', categdetailview, name='categdetail'),
    path('listdetailview/<slug:list>/', listdetailview, name='listdetail'),
    path('team/<slug:team>/', teamdetailview, name="teamdetail"),
    path('team/edit/<slug>/', teamUpdateView.as_view(), name="teamUpdate"),
    path('team/delete/<slug>/', teamDeleteView.as_view(), name="teamDelete"),
    path('list/delete/<slug>/', listDeleteView.as_view(), name="listDelete"),
    path('list/edit/<slug>/', listUpdateView.as_view(), name="listUpdate"),
]