from django.urls import include, path
from rest_framework import routers

from . import views
# from .routers import todo_api_router

router = routers.DefaultRouter()
router.register("hackathons", views.HackathonView)
router.register('user',views.UserView)
router.register('register',views.RegisterView)
router.register('submission',views.SubmissionView)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/listhackathons",views.ListView.as_view(),name="listhackathons"),
    path("api/v1/listsubmissions",views.ListSubmissionView.as_view(),name="listsubmissions"),
    # path('hackathons',views)
]
