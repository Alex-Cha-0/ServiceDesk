# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attachments(models.Model):
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    id_email = models.ForeignKey('Email', models.DO_NOTHING, db_column='id_email', blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Attachments'


class Category(models.Model):
    orderid = models.AutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    ordernumber = models.ForeignKey('Email', models.DO_NOTHING, db_column='orderNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class CategoryChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    thema = models.ForeignKey('ApplicationsThema', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Category_choice'
        unique_together = (('category', 'thema'),)


class Division(models.Model):
    uid = models.AutoField(primary_key=True)
    department = models.TextField(blank=True, null=True)
    email_group = models.TextField(blank=True, null=True)
    user_exchange = models.TextField(blank=True, null=True)
    password_exchange = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Division'


class Staff(models.Model):
    employee = models.TextField(blank=True, null=True)
    uid_division = models.ForeignKey(Division, models.DO_NOTHING, db_column='uid_Division', blank=True, null=True)  # Field name made lowercase.
    email_staff = models.TextField(db_column='email_Staff', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class ApPrinters(models.Model):
    id = models.AutoField()
    model = models.CharField(max_length=50, blank=True, null=True)
    cartridge_model = models.TextField(blank=True, null=True)
    drum_cartridge = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    mac = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    building = models.CharField(max_length=10, blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ap_printers'


class ApplicationsThema(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'applications_thema'


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    message_id = models.AutoField()
    chat_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    datetime_send = models.DateTimeField(blank=True, null=True)
    sender_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'


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


class Email(models.Model):
    subject = models.TextField(blank=True, null=True)
    sender_name = models.TextField(blank=True, null=True)
    sender_email = models.TextField(blank=True, null=True)
    copy = models.TextField(blank=True, null=True)
    datetime_send = models.DateTimeField(blank=True, null=True)
    yes_no_attach = models.BooleanField(blank=True, null=True)
    text_body = models.TextField(blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    specialist = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='specialist', blank=True, null=True)
    control_period = models.DateTimeField(blank=True, null=True)
    date_complited = models.DateTimeField(blank=True, null=True)
    open_order = models.BooleanField(blank=True, null=True)
    close_order = models.BooleanField(blank=True, null=True)
    reply_email = models.BooleanField(blank=True, null=True)
    uid_division = models.ForeignKey(Division, models.DO_NOTHING, db_column='uid_Division', blank=True, null=True)  # Field name made lowercase.
    html_body = models.TextField(blank=True, null=True)
    date_accepted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


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


class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo_content = models.TextField(blank=True, null=True)
    todo_datetime_add = models.DateTimeField(blank=True, null=True)
    todo_due_time = models.DateTimeField(blank=True, null=True)
    todo_in_work = models.BooleanField(blank=True, null=True)
    todo_completed = models.BooleanField(blank=True, null=True)
    todo_email = models.ForeignKey(Email, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todo'
