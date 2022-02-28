from django.urls import path
from . import views, models

app_name = "shows"
urlpatterns = [
    path("shows/", views.ShowsListView.as_view(), name="shows_list"),
    path(
        "shows/anime/",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Anime").order_by(
                "-created_date"
            )
        ),
        name="shows_anime_list",
    ),
    path(
        "shows/action/",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Action").order_by(
                "-created_date"
            )
        ),
        name="shows_action_list",
    ),
    path(
        "shows/drama/",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Drama").order_by(
                "-created_date"
            )
        ),
        name="shows_drama_list",
    ),
    path(
        "shows/<int:id>/", views.ShowsDetailView.as_view(), name="shows_detail"
    ),
    path(
        "shows/<int:id>/update/",
        views.ShowsUpdateView.as_view(), name="shows_update"
    ),
    path(
        "shows/<int:id>/delete/",
        views.ShowsDeleteView.as_view(), name="shows_delete"
    ),
    path("add-shows/", views.ShowsCreateView.as_view(), name="add_show"),
]
