
from django.contrib import admin
"""
Żeby poinformawać django, o tym którymi modelami będziemy zarządzać w panelu
administratora najpierw musimy zaimportawać moduł `admin`, któremu o naszych
predyspozycjach powiemy.

"""

from .models import Post
"""
Już mam komu powiedzieć, ale żeby było jeszcze o czym mówić, musimy
zaimportować nasz model `Post` (czyli definicję naszych danych).

"""

admin.site.register(Post)
"""
Ostateczny krok to rejestracja modelu `Post`. Linia ta mówi: __Hej panelu
administratora django chciał(a)bym zarządząć u Ciebie moimi `Post`-ami__

"""
