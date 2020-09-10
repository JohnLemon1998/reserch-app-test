from django.urls import path
from . import views

urlpatterns = [
        path('test/',views.TestPage,name="test"),
        path('test3/',views.test3,name="test3"),
        path('',views.UserInfo,name="UserInfo"),
        path('hundred/',views.HundredView.as_view(),name="hundred"),
        path('answer/',views.answer,name="answer"),
        path('thankyou/',views.ThankYouView.as_view(),name="thankyou"),
]
