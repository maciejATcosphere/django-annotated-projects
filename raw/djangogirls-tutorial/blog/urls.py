"""
# URLs czyli Uniform Resource Locator

Zanim zaczniemy, załóżmy że Twoja strona będzie zlokalizowana pod adresem:
www.mojasuperdomena.org

"""

# Zanim zaczniemy rozpoznać wzorce adresów stron (ang. url ->
# uniform resource locator) musimy zaimportować do aktulanego kontekstu
# potrzebne nam funkcjonalności.
from django.conf.urls import include, url

# widoki będą nam też potrzebne, to one wykonują ciężką pracę.
from . import views

urlpatterns = [
    # to jest super prosty wzór. Dopasuje się on po prostu do naszej domeny,
    # bez żadnych ekstra znaków. Więc jeżeli użytkownik wpisze
    # www.mojasuperdomena.org, wówczas widok o nazwie `post_list` zostanie
    # odpalony.
    url(r'^$', views.post_list),

    # Dopasuje się do:
    #
    # - www.mojasuperdomena.org/post/123/
    # - www.mojasuperdomena.org/post/0/
    # - www.mojasuperdomena.org/post/547857/
    # - itd.
    # i odpala widok: `post_detail`
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),

    # dopasuje się do: www.mojasuperdomena.org/post/new/
    # i odpala widok: `post_new`
    url(r'^post/new/$', views.post_new, name='post_new'),

    # dopasuje się do:
    #
    # - www.mojasuperdomena.org/post/56/edit/
    # - www.mojasuperdomena.org/post/34/edit/
    # - www.mojasuperdomena.org/post/5748/edit/
    # - itd.
    # i odpala widok `post_edit`
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
