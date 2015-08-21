"""
# Modele w django. Czyli budujemy reprezentację naszych danych.

- Każda aplikacja potrzebuje danych.
- Dane te przechowywane są w bazach danych.
- Istnieje wiele sposobów łączenia się z bazą danych i uzyskiwania dostępu
  do danych.
- Django prosi programistów o opisanie danych, na których nasza aplikacja
  będzie bazować za pośrednictwem tak zwanych modeli.
- Pomyśl o tym jak o modelowaniu jakiegoś obiektu.

"""

# Będziemy musieli zdefinować nasz własny model i żeby to zrobić będziemy
# musieli się dogadać z modelami django.
from django.db import models
# Jedna z właściwości naszego modelu będzie korzystać z aktualnej godziny
# i tutaj pomoże na `timezone`
from django.utils import timezone


class Post(models.Model):
    """
    Naszym podstawowym obiektem będzie Post. Każdy post jest obiektem, który
    ma szereg właściwości, które właśnie czynią go Postem.

    """
    # musimy wiedzieć kto jest autorem każdego postu
    author = models.ForeignKey('auth.User')
    # jaki jest tytuł posta
    title = models.CharField(max_length=200)
    # jego zawartość
    text = models.TextField()
    # kiedy został stworzony. Zwróć uwagę na fakt, że korzystamy tutaj
    # ze wspomniaje funkcjonalności `timezone`, a dokładnie `timezone.now`,
    # która za każdym razem zwraca nam odpowiedź na pytanie:
    # "która jest godzina?"
    created_date = models.DateTimeField(default=timezone.now)
    # oczywiście data stworzenia to nie to samo co data opublikowania. Bo
    # przecież możesz stworzyć post jednego dnia, ale opublikować go znacznie
    # później. Zwróć uwagę na fakt, że to autor bloga musi podać tą datę.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Super użyteczna *metoda*, która pozwala na dodanie daty publikacji,
        prawie że automatycznie.

        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Tutaj mamy do czynienia z prawdziwą magią. Za każdym razem, gdy
        będziesz chciał(a) wypisać (`print`) obiekt typu `Post` na ekranie
        zostanie on zaprezentowany używając jedynie jego tytułu.

        """
        return self.title
        """
        Zwracamy tytuł postu.
        """

"""
Co robi powyższy kod? Czym jest model w django?

- model to definicja obiektu
- definiujemy obiekt za pomocą jego atrybutów.
- to tak jakby ktoś Ciebie spytał o to jak zdefiniwał(a)byś kota?
- pewnie odpowiesz coś w style: "kot to zwierzę, które ma maksimum cztery łapy,
  uszy i imię", czyli w django:

    <pre><code>
    class Cat(models.Model):
        name = models.CharField(max_length=200)
        has_ears = models.BooleanField()
        number_of_legs = models.IntegerField(default=4)
    </pre></code>

"""
