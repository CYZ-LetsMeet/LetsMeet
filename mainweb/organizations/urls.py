from django.urls import path, include, re_path
from .views import MoimListView, MoimDetailView

urlpatterns = [
    path('list/', MoimListView.as_view(), name='moim-list'),
    #path('detail/<uuid:pk>', MoimDetailView.as_view(), name='moim-detail-view'),
    re_path(r'detail/(?P<slug>\w+)/$', MoimDetailView.as_view(), name='moim-detail-view'),
]