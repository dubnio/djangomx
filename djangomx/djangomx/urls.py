from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [

    url(r'^', include('accounts.urls', namespace='accounts')),

    url(r'^', include('newsletter.urls', namespace='subscribe')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^contacto/', include('contact.urls', namespace='contact')),
    url(r'^cursos/', include('courses.urls', namespace='courses')),
    url(r'^ofertas/', include('jobs.urls', namespace='jobs')),

    url(r'^markdown/', include( 'django_markdown.urls')),

    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    url(
        r'^robots\.txt$',
        TemplateView.as_view(
            template_name='robots.txt', content_type='text/plain'
        )
    ),
    url(
        r'^sitemap\.xml$',
        TemplateView.as_view(
            template_name='sitemap.xml', content_type='text/xml'
        )
    ),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
