from cms.utils.compat.dj import is_installed
from django.conf.urls import include, url
from cms.apphook_pool import apphook_pool
from cms.views import details
from django.conf import settings

if settings.APPEND_SLASH:
    reg = url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', details, name='pages-details-by-slug')
else:
    reg = url(r'^(?P<slug>[0-9A-Za-z-_.//]+)$', details, name='pages-details-by-slug')

urlpatterns = [
    # Public pages
    url(r'^example/',
        include('cms.test_utils.project.sampleapp.urls_example', namespace="example1", app_name='example_app')),
    url(r'^example2/',
        include('cms.test_utils.project.sampleapp.urls_example', namespace="example2", app_name='example_app')),
    url(r'^$', details, {'slug': ''}, name='pages-root'),
    reg,
]

if apphook_pool.get_apphooks():
    """If there are some application urls, add special resolver, so we will
    have standard reverse support.
    """
    from cms.appresolver import get_app_patterns
    urlpatterns = get_app_patterns() + urlpatterns


if settings.DEBUG and is_installed('debug_toolbar'):
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
