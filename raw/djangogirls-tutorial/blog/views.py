from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts' :posts})
 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    # pierwszy krok -> sprawdz czy uzytkownik chce zobaczyc PUSTY formularz
    # czy wypelnij juz takowy i wysla nam dane do utworzenia postu

    if request.method == "POST":
        # jezeli trafiles tutaj to znaczy ze uzytkownik kliknal 'save'

        # wezmy dane ktore nam przeslal (znajduja sie one w request.POST) oraz
        # wrzucimy je do naszego formularza
        form = PostForm(request.POST)

        # formularz jest juz wypelnione wiec sprawdzmy czy wszystko jest jak
        # nalezy (is_valid?)
        if form.is_valid():
            # ok wszystko jest super.
            # tworzymy obiekt Post ale jeszcze go nie zapisujemy do bazy danych@
            post = form.save(commit=False)
            # gdyz musimy dodac szybko autora
            post.author = request.user
            # gotowe wiec zapisujemy do bazy danych :-)
            post.save()

            # teraz albo nic nie zrobimy i uzytkonik zobaczy ponownie  strone
            # z formularzem (wypelnionym) albo bedziemy spoko i przekierujemy go
            # REDIRECT do strony gdzie zobaczy efekt swojej pracy
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()

    # jezeli gdzies sie pojawia RETURN to na tym sie zakonczy przetwarzanie
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
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