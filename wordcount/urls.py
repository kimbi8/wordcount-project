"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views # meaning from this directory(under wordcount folder)
                    #import views

urlpatterns = [
    path('', views.home, name = 'home'), #where you want to send
    #path('eggs/',views.eggs) #the user to when they visit homepage
                        # don't add any more information after 'wordcountl.com'
                        #don't forget of the /
    path('count/', views.count, name = 'count'), #the name is passed into the action in the form tag
    path('about/', views.about, name = 'about'), 
]
