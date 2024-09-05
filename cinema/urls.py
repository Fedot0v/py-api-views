from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView,
    ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView,
    CinemaHallViewSet, MovieViewSet
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path(
        "api/cinema/genres/",
        GenreListCreateAPIView.as_view(),
        name="genre-list-create"
    ),
    path(
        "api/cinema/genres/<int:pk>/",
        GenreRetrieveUpdateDestroyAPIView.as_view(),
        name="genre-detail"
    ),
    path(
        "api/cinema/actors/",
        ActorListCreateAPIView.as_view(),
        name="actor-list-create"
    ),
    path(
        "api/cinema/actors/<int:pk>/",
        ActorRetrieveUpdateDestroyAPIView.as_view(),
        name="actor-detail"
    ),
    path("api/", include(router.urls)),
]
