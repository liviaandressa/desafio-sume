"""sume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from cadastro.views import ContasViewSet, UfsViewSet, CidadesViewSet, EnderecosViewSet, PessoasViewSet, OcorrenciasViewSet

router = routers.DefaultRouter()
router.register(r'contas', ContasViewSet)
router.register(r'ufs', UfsViewSet)
router.register(r'cidades', CidadesViewSet)
router.register(r'enderecos', EnderecosViewSet)
router.register(r'pessoas', PessoasViewSet)
router.register(r'ocorrencias', OcorrenciasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

