from django.conf.urls import url

from api.views import course,degreecourse

urlpatterns = [
    url(r"course/",course.CourseAll.as_view({"get":"list","post":"create"})),
    url(r'course/(?P<pk>\d+)/',course.CourseAll.as_view({'get':'retrive',"put":"update","delete":"destory"})),
]