from django.contrib import admin
from django.urls import path
from todo.views import todoView, addTodo, deleteTodo, editTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('editTodo/<int:todo_id>/', editTodo),
]
