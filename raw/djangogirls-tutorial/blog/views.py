"""
# Widoki

Widoki to miejsce w którym wszystko zostaje ostatcznie sklejone. To tutaj
łączymy się z bazą danych, pobieramy nasz szablon i tworzymy kontekst w ramach,
którego pokażemy naszym użytkownikom wymagane przez nich dane.

"""


# Kolejny raz skorzystamy z całego szeregu funkcjonalności, które jest nam dana
# wraz z `django`. Jedną z grup, w której zgromadzona zostało cały szereg
# użytecznych funkcji, jest tzw grupa skrótów (`shortcuts`). Linia ta oznacza: "
# poproszę o dostęp do funkcjonalności: `render`, `get_object_or_404` oraz
# `redirect`, które znajdują się w grupie (module) `shortcuts` będącą częścią
# `django`"
from django.shortcuts import render, get_object_or_404, redirect

# django oprócz skrótów ma cały szereg przydatnych funkcji (ang. utilities lub
# w skrócie `utils`). Jedną z nich jest `timezone`, która pozwala nam na m.in.
# sprawdzenie aktulanej godziny.
from django.utils import timezone

# Nasi użytkownicu będę przesyłać nam prośby związane z `Post`-ami, w związku
# z czym model `Post` również musi zostać zaimportowany pliku widoków
# kontekstu.
from .models import Post

# Będziemy wyświetlać listę `Post`-ów, pojedyncze `Post`-y oraz naturalnie
# pozwolimy naszym użytkownikom na tworzenie nowych `Post`-ów, w tym właśnie
# zadaniu pomoże nam `PostForm`.
from .forms import PostForm


def post_list(request):
    """
    Jeżeli odwrócisz kolejnoć słów w nazwie tego widoku (funkcji) oraz
    przetłumaczysz ją na język polski wówczas otrzymasz kolejno:

    - `post_list` -> `list post` (po odwórceniu kolejności)
    - `list post` -> `wylistuj post(y)` (po przetłumaczniu na polski :-) )

    I to właśnie robi ten widok: listuje posty.

    """
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    """
    posty które wyświetlimy naszym użytkownikom muszą zostać pobrane
    z bazy danych. Jednak nie chcemy pokazać im wszystkich istniejących
    postów, ponieważ w naszej bazie danych mogą istnieć posty, dla
    których jest jeszcze o wiele za wcześnie na publikację. Instrukcja
    `published_date__lte=timezone.now()` powinna być interpretowana jako:
    "data publikacji (`published_date`) mniejsza równa (`__lte`) aktualnej
    dacie (`timezone.now()`)". Instrukcja `.order_by('published_date')`
    powinna być czytana jako: "posortuj względem daty publikacji
    (`published_date`) zaczynając od najstarszej daty". Więc jeżeli
    zbierzesz to wszystko razem te skromne dwie linie mówią: "pobierz
    z bazy danych wszystkie posty, których daty publikacji są wcześniejsze
    lub równe aktulanej dacie, oraz tak uzyskane posty posortuj według
    tejże daty publikacji rosnąco"

    """

    return render(request, 'blog/post_list.html', {'posts': posts})
    """
    Ok. Interesujące posty znajdują się w `posts` więc teraz trzeba
    wygenerować (wyrenderować) naszą stronę, używając szablonu o nazwie
    `post_list.html`. I tak właśnie wygenerowaną stronę przesyłamy (`return`)
    do naszego użytkownika.

    """


def post_detail(request, pk):
    """
    Patrząc na nazwę tego widoku, jak sądzisz jakie jego jego zadanie?
    Naturalnie: "pokaż szczegółowe dane odnośnie konkretnego postu". Ale, skąd
    wiemy jakie konkretnie post pokazać? Pomoże nam w tym `pk`
    (ang. primary key), które kryje w sobie *unikatowy* numer, które jest
    przypisane do każdego postu w trakcie jego narodzin :-)

    """

    post = get_object_or_404(Post, pk=pk)
    """
    Mówimy w skrócie: "pobierz post of unikatowych numerze przechowywanych
    w zmiennej `pk`, a jeżeli takowy post nie istnieje wyświetl użytkownikowi
    wiadomość 404."
    FIXME: show some nice image about 404. (as a side comment)

    """

    return render(request, 'blog/post_detail.html', {'post': post})
    """
    Instrukcja ta wygląda niemal identycznie jak tak na końcu widoku
    `post_list`. Mówi ona: "Zwróć użytkownikowi stronę wygenerowaną z
    szablonu `post_detail.html` używając danych zawartych w zmiennej `post`."

    """


def post_new(request):
    """
    Widok ten obsługuje wszelkie prośby a propos utworzenia nowego postu.

    """

    if request.method == "POST":
        """
        jeżeli trafileś/trafiłaś tutaj to znaczy, że użytkownik kliknął `save`

        """

        form = PostForm(request.POST)
        """
        weźmy dane które nam przesłał (znajdują się one w `request.POST`) oraz
        wrzucimy je do naszego formularza

        """

        if form.is_valid():
            """
            formularz jest juz wypelnione wiec sprawdzmy czy wszystko jest jak
            nalezy (is_valid?)

            """

            post = form.save(commit=False)
            """
            ok wszystko jest super. Tworzymy obiekt `Post` ale jeszcze go
            nie zapisujemy do bazy danych,

            """
            post.author = request.user
            """
            gdyż musimy dodać szybko autora.

            """

            post.save()
            """
            gotowe wiec zapisujemy do bazy danych :-)

            """

            return redirect('blog.views.post_detail', pk=post.pk)
            """
            teraz przekierujemy naszego wiernego użytkownika
            (ang. `redirect`) do strony gdzie zobaczy efekt swojej pracy.

            """
    else:
        form = PostForm()
        """
        skoro tutaj trafiliśmy to znaczy to, że użytkownik nie wcisnął
        przycisku `save` ale po prostu nas poprosił o wyświetlenie strony
        z pustym formularzem, czy wiesz skąd ja to wiem?

        """

    return render(request, 'blog/post_edit.html', {'form': form})
    """
    Na tym etapie na formularz jest pusty więc wygenerujmy stronę na której
    go pokażemy.

    """


def post_edit(request, pk):
    """
    Widok ten pomoże nam edytować już istniejący post.

    """

    post = get_object_or_404(Post, pk=pk)
    """
    Zanim zaczniemy musimy pobrać post, który właśnie edytować chcemy.

    """

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
