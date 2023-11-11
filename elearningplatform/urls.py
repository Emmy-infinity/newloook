from django.urls import path
from.import views
app_name="elearningplatform"
urlpatterns= [ path("",views.home, name="home"),
             path("Note/",views.Notes,name='Notes'),
             path("video/",views.Videos, name="video"),
             path('register/',views.registerPage,name='register'),
             path('About/',views.About ,name='About'),
             path('Article/',views.Article,name='Article'),
             path('quizz/',views.quizz,name='quizz'),
             
             path('Learningmaterials/',views.Learning_materials,name='LearningMaterials'),
             path ('privacypolicy/',views.PrivacyPolicy,name='Privacy Policy'),
             ]