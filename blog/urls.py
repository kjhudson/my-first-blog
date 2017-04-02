'''We aare importing Django's function url
 and all of our views from blog application
'''
from django.conf.urls import url
from . import views

'''we are assigning a view called post_list to ^$ URL
    which will match only an empty string ^ nothing $ end
    http://127.0.0.1:8000/ is not part of the url in Django
    pattern tells Django the views.post_list ir the right place
    to go if someone enters the website at http://127.0.0.1:8000/
''' 


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
