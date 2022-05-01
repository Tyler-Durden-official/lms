from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin_home/", views.dashboard, name="dashboard"),
    path("add_book/", views.add_book, name="add_book"),
    path("permission_manager/", views.permission_manager, name="permission_manager"),
    path("request_book/", views.request_book, name="request_book"),
    path("view_books_admin/", views.view_books_admin, name="view_books_admin"),
    path("view_books_student/", views.view_books_student, name="view_books_student"),
    path("view_students/", views.view_students, name="view_students"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("view_requested_book/", views.view_requested_book, name="view_requested_book"),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),
    path("student_requested_books/", views.student_requested_books, name="student_requested_books"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("student_registration/", views.student_registration, name="student_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("student_login/", views.student_login, name="student_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_issue/<int:myid>/", views.delete_issue, name="delete_issue"),
    path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
    path("accept_request/<int:myid>/", views.accept_request, name="accept_request"),
    path("delete_request/<int:myid>/", views.delete_request, name="delete_request"),
    path("reject_request/<int:myid>/", views.reject_request, name="reject_request"),
    path("cancel_request/<int:myid>/", views.cancel_request, name="cancel_request"),
    path("student_track_request/<int:myid>/", views.student_track_request, name="student_track_request"),
    path("admin_track_request/<int:myid>/", views.admin_track_request, name="admin_track_request"),
    path("send_email/<str:branch>/", views.send_email, name="send_email"),
    path("view_hods/", views.view_hods, name="view_hods"),
    path("add_hod/", views.add_hod, name="add_hod"),
    path("edit_hod/<int:myid>/", views.edit_hod, name="edit_hod"),
]