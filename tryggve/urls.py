from django.urls import path
from tryggve import views
from django.views.generic import TemplateView

urlpatterns = [
    # Glyph page and homepage
    path('', TemplateView.as_view(template_name="tryggve/tryggve.html"), name="tryggve-view"),
    
    # Urls to the navbar
    path('about/', TemplateView.as_view(template_name="tryggve/about.html"), name="about-view"),
    path('resources/', TemplateView.as_view(template_name="tryggve/resources.html"), name="resources-view"),
    path('team/<int:pk>/', views.CountryView.as_view(), name="country-view"),
    path('infrastructure/', TemplateView.as_view(template_name="tryggve/infrastructure.html"), name="infrastructure-view"),
    path('funding/', TemplateView.as_view(template_name="tryggve/funding.html"), name="funding-view"),
    path('projects/', TemplateView.as_view(template_name="tryggve/projects.html"), name="projects-view"),
    path('news/', TemplateView.as_view(template_name="tryggve/news.html"), name="news-view"),
    path('jobs/', TemplateView.as_view(template_name="tryggve/jobs.html"), name="jobs-view"),
    
    # for testing stufff
    path('test/', views.TestView.as_view(), name="test-view"),
    path('test2/', TemplateView.as_view(template_name="tryggve/PRS_in_S3.html"), name="test2-view"),
    
]