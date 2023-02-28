from django.urls import path
from todo_app import views
urlpatterns = [
    path('todo-lists', views.todo_lists_handler),
    path('todo_lists/<int:pk>', views.todo_list_handler),
    path('todo_lists/<int:pk>/todos', views.todo_list_todos_handler),
    # # path('todos'),
    path('todos/<int:pk>', views.todo_handler)

]