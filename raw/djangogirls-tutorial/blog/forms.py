from django import forms
"""
Stworzymy formularz django, który naturalnie będzie korzystał z już istniejcej
funkcjonalności formularzy django.

"""

from .models import Post
"""
Nasz formularz pomoże nam tworzyć nowe `Post`-y

"""

class PostForm(forms.ModelForm):
    """
    Linia ta mówi: "Chciał(a)bym zdefiniować formularz o nazwie `PostForm`
    który pomoże mi zarządzać jednym z moich modeli"

    """

    class Meta:
        model = Post
        """
        Tym modelem będzie oczywiści `Post`

        """

        fields = ('title', 'text',)
        """
        oraz nasz formularz będzie się miał dwa pola, odpowiednio dla
        tytułu i zawartości naszego postu.

        """
