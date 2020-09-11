from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',VariantList.as_view()),
    path('variant/<int:pk>/',QuestionsView.as_view(),name="variant"),
    path('themes/<int:pk>/',ThemeDetail.as_view(),name="theme")
]
