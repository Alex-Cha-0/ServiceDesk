# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.utils import timezone

printer = 'Prnt'
server = 'Srv'
software = 'Soft'
helpUser = 'Help'
video = 'Vdo'
one_c = '1c'
lan = 'lan'

TYPE_CHOICES = (
    (printer, 'Оргтехника'),
    (server, 'Сервера'),
    (software, 'Программное обеспечение'),
    (helpUser, 'Помощь пользователям'),
    (video, 'Видеонаблюдение'),
    (one_c, '1c'),
    (lan, 'Монтаж лвс'),
)


class Thema(models.Model):
    name = models.CharField(max_length=5, choices=TYPE_CHOICES, unique=True)

    class Meta:
        managed = True
        verbose_name = 'Категории работ'

    def __str__(self):
        return self.get_name_display()


class Attachments(models.Model):
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    id_email = models.ForeignKey('Email', on_delete=models.CASCADE, db_column='id_email', blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Attachments'

    def __str__(self):
        return str(self.id_email)

    def slice_string(self):
        s = self.name
        last_dot_index = s.rfind('.')  # Находим индекс последнего символа '.'

        if last_dot_index != -1:  # Если символ '.' найден
            sliced_string = s[last_dot_index:]  # Делаем срез строки до последнего символа '.'
            return sliced_string
        else:
            return s  # Возвращаем исходную строку, если символ '.' не найден


class Category(models.Model):
    orderid = models.AutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    ordernumber = models.ForeignKey('Email', on_delete=models.DO_NOTHING,
                                    db_column='orderNumber',
                                    related_name='category_order_number')  # Field name made lowercase.
    createddate = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    choice = models.ManyToManyField(Thema)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Category'
        verbose_name = 'Категории'

    def __str__(self):
        return str(self.orderid)


class CategoryChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thema = models.ForeignKey('Thema', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Category_choice'
        unique_together = (('category', 'thema'),)
        verbose_name = 'Выбранные категории'

    def __str__(self):
        return str(self.category)


class Division(models.Model):
    uid = models.AutoField(primary_key=True)
    department = models.TextField(blank=True, null=True)
    email_group = models.TextField(blank=True, null=True)
    user_exchange = models.TextField(blank=True, null=True)
    password_exchange = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.uid)

    class Meta:
        managed = False
        db_table = 'Division'


class Staff(models.Model):
    employee = models.TextField(blank=True, null=True)
    uid_division = models.ForeignKey(Division, models.DO_NOTHING, db_column='uid_Division', blank=True,
                                     null=True)  # Field name made lowercase.
    email_staff = models.TextField(db_column='email_Staff', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    def __str__(self):
        return self.employee

    def get_absolute_url(self):
        return reverse('specialist', kwargs={'specialist_id': self.id})

    class Meta:
        managed = False
        db_table = 'Staff'
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ['-id']


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

    def __str__(self):
        return f"{self.user} {self.group}"


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    message_id = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey('Email', on_delete=models.CASCADE, blank=True, null=True, db_column='chat_id')
    user_name = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    datetime_send = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    sender_id = models.IntegerField(blank=True, null=True, db_column='sender_id')

    class Meta:
        managed = True
        db_table = 'chat'
        ordering = ['-datetime_send']

    def __str__(self):
        return str(self.chat_id)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(blank=True, null=True, max_length=150)
    email = models.CharField(blank=True, null=True, max_length=254)
    order_id = models.ForeignKey('Email', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        ordering = ['author']

    def __str__(self):
        return self.author


class Email(models.Model):
    subject = models.TextField(blank=True, null=True)
    sender_name = models.TextField(blank=True, null=True)
    sender_email = models.TextField(blank=True, null=True)
    copy = models.TextField(blank=True, null=True)
    datetime_send = models.DateTimeField(blank=True, null=True)
    yes_no_attach = models.BooleanField(blank=True, null=True)
    text_body = models.TextField(blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    specialist = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='specialist', blank=True, null=True,
                                   related_name='spec')
    control_period = models.DateTimeField(blank=True, null=True)
    date_complited = models.DateTimeField(blank=True, null=True)
    open_order = models.BooleanField(blank=True, null=True)
    close_order = models.BooleanField(blank=True, null=True)
    reply_email = models.BooleanField(blank=True, null=True)
    uid_division = models.ForeignKey(Division, models.DO_NOTHING, db_column='uid_Division', blank=True,
                                     null=True)  # Field name made lowercase.
    html_body = models.TextField(blank=True, null=True)
    date_accepted = models.DateTimeField(blank=True, null=True)
    is_chat = models.BooleanField(blank=True, null=True)
    author = models.ForeignKey(OrderAuthor, models.DO_NOTHING, blank=True,
                               null=True, related_name='author_order')

    def get_absolute_url(self):
        return reverse('applications:message', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id)

    @property
    def is_past_due(self):
        try:
            return timezone.now() > self.control_period
        except Exception as s:
            pass

    class Meta:
        managed = False
        db_table = 'email'
        ordering = ['-datetime_send']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
