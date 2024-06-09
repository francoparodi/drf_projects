from django.urls import path
from .views import FileUploadView, SolutionListCreateView, SolutionDetailView, SolutionDeleteView, SolutionUpdateView

urlpatterns = [
    path('solutions/', SolutionListCreateView.as_view(), name='solution-list-create'),
    path('solutions/<int:pk>/', SolutionDetailView.as_view(), name='solution-detail'),
    path('solutions/delete/<int:pk>/', SolutionDeleteView.as_view(), name='solution-delete'), 
    path('solutions/update/<int:pk>/', SolutionUpdateView.as_view(), name='solution-update'), 
    path('upload/', FileUploadView.as_view(), name='file-upload'),

]