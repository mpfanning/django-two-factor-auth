from django.conf.urls import url

from .views import TwilioCallApp

urlpatterns = [
    url(
        regex=r'^twilio/inbound/two_factor/(?P<token>\d+)/$',
        view=TwilioCallApp.as_view(),
        name='twilio_call_app',
    ),
]
