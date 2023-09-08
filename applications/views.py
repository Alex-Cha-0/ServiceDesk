from datetime import datetime
import time
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from todo_list.models import ToDo
from .models import *
from .forms import AddOrder, UserRegisterForm, UserLoginForm, ContactForm, CategoryChoiceForm
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import EmailMessage
from bs4 import BeautifulSoup
from django.db.models import Count


@login_required
def close_order(request, message_id):
    data_email = Email.objects.get(id=message_id)
    if request.method == 'POST':
        form = CategoryChoiceForm(request.POST, initial={'ordernumber': message_id})
        if form.is_valid():
            data_email.open_order = 0  # change field
            data_email.close_order = 1
            data_email.date_complited = datetime.now()
            data_email.save()

            form.save()
            return redirect(f'/applications/message/{message_id}')
    else:

        form = CategoryChoiceForm(initial={'ordernumber': message_id})

    return render(request, 'add_category.html', {"form": form})


@login_required
def send_email(request, message_id):
    email_data = Email.objects.get(id=message_id)
    chat_data = Chat.objects.filter(chat_id=message_id)

    def edit_body(html_body, content):
        soup = BeautifulSoup(html_body, 'html.parser')

        new_p = soup.new_tag("p")
        new_p2 = soup.new_tag('p')
        new_hr = soup.new_tag('hr')
        new_p.string = content
        new_p2.string = 'date: ' + str(datetime.now())
        div_tag = soup.find('div')
        solid_hr = soup.new_tag('hr')
        solid_hr['style'] = " height: 12px;" \
                            "border: 0;" \
                            "box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);"

        div_tag.insert_before(new_p, new_p2, new_hr)

        for i in chat_data:
            # hr = soup.new_tag('hr')
            # hr['style'] = " border: 0;" \
            #               "height: 0;" \
            #               "border-top: 1px solid rgba(0, 0, 0, 0.1);" \
            #               "border-bottom: 1px solid rgba(255, 255, 255, 0.3);"
            chat_div = soup.new_tag("div")
            chat_username = soup.new_tag("h5")
            chat_content = soup.new_tag("p")
            chat_datetime = soup.new_tag("small")

            if i.sender_id == 1:
                # Blue color

                chat_username.string = i.user_name
                chat_content.string = i.content
                chat_datetime.string = str(i.datetime_send)
                chat_div.insert(1, chat_username)
                chat_div.insert(2, chat_content)
                chat_div.insert(3, chat_datetime)
                chat_div['style'] = "margin-right: 50px;" \
                                    "float: left;" \
                                    "font-family: cursive;" \
                                    "border: 1px solid black;" \
                                    "border-radius: 6px;"
                div_tag.insert_before(chat_div)
            else:
                # Orange color

                chat_username.string = i.user_name
                chat_content.string = i.content
                chat_datetime.string = str(i.datetime_send)
                chat_div.insert(1, chat_username)
                chat_div.insert(2, chat_content)
                chat_div.insert(3, chat_datetime)
                chat_div['style'] = "float: right;" \
                                    "margin-left: 50px;" \
                                    "text-align: right;" \
                                    "font-family: cursive;" \
                                    "border: 1px dashed black;" \
                                    "border-radius: 6px;"
                div_tag.insert_before(chat_div)

        # div_tag.insert_before(new_p, new_p2, new_hr)
        my_html_string = str(soup).replace("'", '')
        return my_html_string

    if request.method == 'POST':
        form = ContactForm(request.POST,
                           initial={'subject': f're: {email_data.subject}', 'to': email_data.author.email, 'cc_myself': email_data.copy})

        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            to = [form.cleaned_data['to']]
            cc = [form.cleaned_data['cc_myself']]

            mail = EmailMessage(subject=subject, body=edit_body(email_data.text_body, content),
                                from_email=settings.EMAIL_HOST_USER, to=to, cc=cc)
            mail.content_subtype = 'html'
            mail.send(fail_silently=False)

            chat_create = Chat.objects.create(user_name=f"{request.user.last_name} {request.user.first_name}",
                                              content=content, sender_id=1)
            email_data.chat_set.add(chat_create)

            if email_data.is_chat:
                pass
            else:
                email_data.is_chat = True

            email_data.save()

            if mail.send:
                messages.success(request, 'Письмо отправлено')
                return redirect(f'/applications/message/{message_id}')
            else:
                messages.error(request, 'Ошибка отправки')
    else:
        # form = ContactForm()
        form = ContactForm(
            initial={'subject': f're: ##{message_id}## {email_data.subject}', 'to': email_data.sender_email})

    return render(request, 'send_email.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна')
            return redirect('applications:home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('applications:home')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('applications:login')


# class NewGetMessage(MyMixin, ListView):
#     model = Email
#     template_name = 'index.html'
#     context_object_name = 'content'
#     paginate_by = 15
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(NewGetMessage, self).get_context_data(**kwargs)
#         context['title'] = self.get_upper('Главная страница')
#         message_id = self.kwargs.get('pk', None)
#         context['data'] = Email.objects.get(id=message_id)
#         context['attachment'] = Attachments.objects.filter(id_email=message_id)
#         context['dir'] = settings.DIRECTORY_ATTACHMENTS
#         return context
#
#     def get_queryset(self):
#         return Email.objects.filter(close_order=False)


class HomeApp(MyMixin, ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeApp, self).get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        # message_id = self.kwargs.get('message_id', None)
        # context['data_message'] = Attachments.objects.all()

        return context


class HomeByAccepted(ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15
    queryset = Email.objects.filter(open_order=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Принятые'
        context['accepted_by'] = f'Accepted by all'
        return context


class AcceptedByUser(ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Accepted by {self.request.user}'
        context['accepted_by'] = f'Accepted by {self.request.user}'
        return context

    def get_queryset(self):
        return Email.objects.filter(specialist=self.request.user.id, open_order=True)


class HomeByClosed(ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15
    queryset = Email.objects.filter(close_order=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Закрытые'
        return context


class HomeByNew(ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15
    queryset = Email.objects.filter(Q(open_order=None, close_order=None) | Q(open_order=False, close_order=False))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новые'
        return context


class GetSpecialist(ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Staff.objects.get(pk=self.kwargs['specialist_id'])
        return context

    def get_queryset(self):
        return Email.objects.filter(specialist_0=self.kwargs['specialist_id'])


class GetMessage(LoginRequiredMixin, DetailView):
    model = Email
    template_name = "message.html"
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GetMessage, self).get_context_data(**kwargs)
        message_id = self.kwargs.get('pk', None)
        context['attachment'] = Attachments.objects.filter(id_email=message_id)
        context['dir'] = settings.DIRECTORY_ATTACHMENTS
        context['chat_data'] = Chat.objects.filter(chat_id=message_id)
        try:
            context['category'] = Category.objects.get(ordernumber=message_id)
        except Exception as s:
            print(s)

        context['users_from_active_group'] = User.objects.filter(groups__name=self.request.user.groups.get().name)
        return context


class CreateOrder(LoginRequiredMixin, CreateView):
    form_class = AddOrder
    template_name = 'add_order.html'
    # raise_exception = True


# def add_order(requests):
#     if requests.method == 'POST':
#         form = AddOrder(requests.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # Email.objects.create(**form.cleaned_data)  # Распаковка словара
#             email = form.save()
#
#     else:
#         form = AddOrder()
#     return render(requests, 'add_order.html', {'form': form})

# class CloseOrder(CreateView):
#     form_class = CategoryForm
#     template_name = 'add_category.html'


# class CloseOrder(LoginRequiredMixin, ListView):
#     model = Email
#     template_name = 'index.html'
#     context_object_name = 'content'
#     paginate_by = 15
#     raise_exception = True
#
#     def get_queryset(self):
#         message_id = self.kwargs.get('message_id', None)
#         mod = Email.objects.get(id=message_id)
#         mod.open_order = 0  # change field
#         mod.close_order = 1
#         mod.date_complited = datetime.now()
#         mod.save()
#         return Email.objects.filter(close_order=False)


class OpenOrder(LoginRequiredMixin, ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15
    raise_exception = True

    def get_queryset(self):
        message_id = self.kwargs.get('message_id', None)
        mod = Email.objects.get(id=message_id)
        spec = AuthUser.objects.get(id=self.request.user.id)  # Получение id пользователя
        mod.open_order = 1  # change field
        mod.close_order = 0
        mod.specialist = spec
        mod.control_period = mod.datetime_send + timedelta(days=10)
        mod.date_accepted = datetime.now()
        mod.save()
        return Email.objects.filter(close_order=False)


@login_required
def message_open_order(requests, message_id):
    mod = Email.objects.get(id=message_id)
    spec = AuthUser.objects.get(id=requests.user.id)
    mod.open_order = 1  # change field
    mod.close_order = 0
    mod.specialist = spec
    mod.control_period = mod.datetime_send + timedelta(days=10)
    mod.date_accepted = datetime.now()
    mod.save()
    # model = Email.objects.all().order_by('-id')
    # context = {
    #     'content': model
    # }
    return redirect(f'/applications/message/{message_id}')


# def close_order(requests, message_id):
#     mod = Email.objects.get(id=message_id)
#     mod.open_order = 0  # change field
#     mod.close_order = 1
#     mod.save()
#     model = Email.objects.all().order_by('-id')
#     context = {
#         'content': model
#     }
#     return render(requests, 'index.html', context)

class DeleteOrder(LoginRequiredMixin, ListView):
    model = Email
    template_name = 'index.html'
    context_object_name = 'content'
    paginate_by = 15
    raise_exception = True

    def get_queryset(self):
        message_id = self.kwargs.get('message_id', None)
        mod = Email.objects.get(id=message_id)
        mod.delete()
        return Email.objects.filter(close_order=True)


class Cabinet(LoginRequiredMixin, DetailView):
    template_name = 'cabinet.html'
    queryset = AuthUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        try:
            context = super(Cabinet, self).get_context_data(**kwargs)
            user_id = self.kwargs.get('pk', None)
            context['email_data'] = Email.objects.select_related().filter(specialist=user_id)
            context['author'] = (set(OrderAuthor.objects.filter(author_order__specialist_id=user_id)))
            context['active'] = Email.objects.filter(specialist=user_id, open_order=True).count()
            context['success'] = Email.objects.filter(specialist=user_id, close_order=True).count()
            context['is_past'] = Email.objects.filter(specialist=user_id, control_period__lt=timezone.now(),
                                                      open_order=True).count()
            context['todo'] = ToDo.objects.filter(todo_spec=user_id, todo_completed=False)
            # context['count_data_orders'] = Email.objects.annotate(total_orders=Count('orderauthor') )

            return context
        except Exception as s:
            pass
        finally:
            return context


@permission_required("app_email.change_app_email")
def add_spec(request, message_id):
    # получаем из данных запроса POST отправленные через форму данные
    spec = request.POST.get("specialist", "Undefined")
    mod = Email.objects.get(id=message_id)
    spec_ = AuthUser.objects.get(username=spec)
    mod.specialist = spec_
    mod.save()
    return redirect(f'/applications/message/{message_id}')


@permission_required("app_email.change_app_email")
def extend_the_period(request, message_id):
    date = request.POST.get("date")
    mod = Email.objects.get(id=message_id)
    mod.control_period = date
    mod.save()
    return redirect(f'/applications/message/{message_id}')
