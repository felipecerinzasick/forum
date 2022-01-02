from django.urls import path

from .views import (
    HomeView, NewCampaignView, NewPageView, DeletePageView,
    CopyJsCode, AllPageView, TrafficCounter
)

app_name = 'analytics'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-campaign/', NewCampaignView.as_view(), name='new-campaign'),
    path('new-page/', NewPageView.as_view(), name='new-page'),
    path('delete-page/<int:pk>', DeletePageView.as_view(), name='delete-page'),
    path('copy-code/', CopyJsCode.as_view(), name='copy-code'),
    path('report/', AllPageView.as_view(), name='report'),
    path('traffic/', TrafficCounter.as_view())
]
