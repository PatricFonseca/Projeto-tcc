from django.conf.urls import url
from views import index
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls))
    url(r'^$', index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', exibirPerfil, name='exibirPerfil')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)