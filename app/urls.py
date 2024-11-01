from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download-db/', views.download_database, name='download_database'),
    # path('increment/', views.increment_count, name='increment_count'),
    # path('decrement/', views.decrement_count, name='decrement_count'),
]
