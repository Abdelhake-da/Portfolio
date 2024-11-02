from django.urls import path


from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('get_project/', views.get_project, name='get_project'),
    path('download-db/', views.download_database, name='download_database'),

    path("counter/", views.counter_page, name="counter_page"),
    path("counter/update/", views.counter_view, name="counter_update"),

    path("comments/", views.comment_page, name="comment_page"),
    path("comments/add/", views.add_comment, name="add_comment"),
]
