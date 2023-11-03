from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import BookmarkForm, UserRegisterForm
from .models import Bookmark, User

from .tasks import parse_and_save_link

class IndexView(TemplateView):
    template_name = 'bookmarks/index.html'


def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            url = request.POST.get('url')
            if not Bookmark.objects.filter(user_id=user_id, url=url).exists():  
                parse_and_save_link(url, user_id)  # Запускаем таск асинхронно
            else:
                messages.warning(request, 'Указанная ссылка уже есть в закладках')
            return redirect('bookmark_list')
    else:
        form = BookmarkForm()
    context = {'form': form}
    return render(request, 'bookmarks/add_bookmark.html', context)

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user)  # Получение всех закладок, принадлежащих текущему пользователю
    context = {'bookmarks': bookmarks}
    return render(request, 'bookmarks/bookmarks_list.html', context)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'bookmarks/register.html'
    success_url = '/login'