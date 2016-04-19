from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/profile/$', 'cms_templates.views.usuario'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/$', 'cms_templates.views.muestra_todo'),
    url(r'^annotated/(\d+)', 'cms_templates.views.busca_pagina'),
    #url(r'^annotated/anadir/formulario', 'cms_templates.views.crea_pagina'),
    url(r'^annotated/anadir', 'cms_templates.views.nueva_pagina'),
    url(r'^admin/', include(admin.site.urls)),
)
