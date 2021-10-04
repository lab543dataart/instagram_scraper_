from django.urls import path

from board_app import views

app_name = "boardapp"


urlpatterns = [
    path('', views.post, name="board"),
    path('write/', views.board, name="write"),
    path('post/<int:id>', views.detail, name='detail'),

    #다운로드를 위한 경로 설정
    path('export_user_xls/<int:id>', views.export_users_xls, name="excel")
]