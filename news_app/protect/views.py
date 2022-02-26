from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.utils import timezone
from django.shortcuts import redirect, render
import pytz


# (1)
# (2)
class IndexView(LoginRequiredMixin, TemplateView):
    # template_name = 'protect/index.html'

    def get(self, request, **kwargs):
    # def get(self, request):

        curent_time = timezone.now()

        context = {
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones
        }
        return HttpResponse(render(request, 'protect/index.html', context))

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')

    # (3)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['is_authors'] = self.request.user.groups.filter(name='authors').exists()
        return context


""" 

(1)
generic-представление для отображения шаблона из папки templates, которую мы сами создали и путь до нее прописали
в файле-настройке проекта settings.py / TEMPLATES / 'DIRS': [os.path.join(BASE_DIR, 'templates')] (+импорт модуля os),
либо просто можно написать, 'DIRS': [BASE_DIR/'templates'], но хз, вызывало ошибку как-то раз
(2)
данный шаблон protect/index.html запускается, если мы в приложении sign прошли аутентификацию (в соответствии
с нашей логикой приложения),  LoginRequiredMixin - нужен для того, чтоб данный класс понял, что можно
запускать представление, что пользователь зарегистрирован в системе
(3)
в общем в двух словах, как эта богодельня работает:
мы создаем на нашей html страничке тег, например как в нашем случае (2) {% if is_not_authors %}_______{% endif %}
помещаем вместо подчеркиваний какой-то код, например кнопку в нашем случае, и если выполняется условие (после
равно (3-8)), то данный код появится на странице, если не выполняется условие, то код не появится, все просто

данная функция дает возможность добавлять в наше представление дополнительные отображения, например в нашем случае
добавить отображение кнопки в зависимости от того, в какой группе находится наш пользователь, если он не автор
еще, то кнопку отображать, если он становится автором, то кнопку убрать

(4)
получаем весь контекст из класса-родителя
добавили (1) новую контекстную переменную is_not_authors (2), чтобы ответить на вопрос, есть ли пользователь
в группе, мы заходим в переменную запроса self.request (4), из этой переменной мы можем вытащить текущего
пользователя, в поле groups хранятся все группы (5), в которых он состоит, далее применяем фильтр к этим
группам (6) и ищем ту самую, имя которой authors (7), после чего проверяем, есть ли какие-то значения
в отфильтрованном списке (8), метод exists() - с англ означает "существует", данная конструкция вернет
True, если группа authors в списке групп пользователя найдена, иначе — False, в нашем случае нужно получить
наоборот — True (то есть кнопка видима), если пользователь не находится в этой группе, поэтому добавляем
отрицание not, и возвращаем контекст, важно filter(name = 'authors') чтоб группы совпадали 'authors'
суть данного метода в том, чтоб убрать кнопку, когда пользователь находится в группе, если он не находится
то кнопка видимая остается
________1__________2____________3_______4_______________5_______6____________7_________8
if not self.request.user.groups.filter(name='authors').exists():
    context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()

"""