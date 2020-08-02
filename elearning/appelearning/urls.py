from django.urls import path

from . import views
 
app_name = 'appelearning'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/resetpassword/', views.PasswordResetedView.as_view(), name='password_reset'),
    path('resetpassword/resetpassworddone/', views.PasswordResetedDoneView.as_view(), name='password_reset_done'),
    path('/overview/', views.OverviewView.as_view(), name='overview'),
    path('/overview/adduser/', views.CreateUserView.as_view(), name='adduser'),
    path('/overview/updateuser/<int:pk>', views.UpdateUserView.as_view(), name='updateuser'),
    path('', views.LogoutView.as_view(), name='logout'),
    path('/overview/addcourse/', views.CreateCourseView.as_view(), name="addcourse"),
    path('/addtest/', views.CreateTestView.as_view(), name='createtest'),
    path('/overview/course/maketest/<int:pk>', views.MakeTestView.as_view(), name='maketest'),
    path('/overview/course/testprofile/<int:pk>', views.MulitpleChoiceTestProfileView.as_view(), name="testprofile"),
    path('/overview/course/maketest/checkSolutions/', views.checkSolutions, name="checkSolutions"),
    path('/course/update/<int:pk>', views.UpdateCourseView.as_view(), name="updatecourse"),
    path('/course/profile/<int:pk>', views.ProfileCourseView.as_view(), name="courseprofile"),
    path('/overview/course/tests/', views.ShowTestsView.as_view(), name="alltests"),
    path('/overview/course/tests/results/', views.ShowResultsView.as_view(), name="showresults"),
    path('/overview/course/tests/question/profile/<int:pk>', views.ShowQuestionView.as_view(), name="questionprofile"),
    path('/overview/course/delete/<int:pk>', views.DeleteCourseView.as_view(), name="deletecourse"),
]