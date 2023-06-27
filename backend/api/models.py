from django.db import models


class BaseModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Users(BaseModel):
  id = models.AutoField(auto_created=True, primary_key=True)
  full_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=255, unique=True)
  avatar_url = models.URLField(null=True, blank=True)

  class Meta:
    db_table = "users"


class Profiles(BaseModel):
  id = models.AutoField(auto_created=True, primary_key=True)
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  grade = models.CharField(max_length=10)
  birth = models.DateField()
  gender = models.CharField(max_length=20)
  nationality = models.CharField(max_length=30)
  hometown = models.TextField(null=True)
  address = models.TextField(null=True)
  phone_number = models.CharField(max_length=20)
  parents_name = models.CharField(max_length=50)
  parents_occupation = models.CharField(max_length=50)
  other_information = models.TextField(null=True)

  class Meta:
    db_table = "profiles"


class Organizations(BaseModel):
  class OrganizationType(models.TextChoices):
    SCHOOL = 0
    CLASS = 1

  id = models.AutoField(auto_created=True, primary_key=True)
  type = models.IntegerField(default=0)
  name = models.CharField(max_length=255)
  organization_id = models.IntegerField(default=0)

  class Meta:
    db_table = "organizations"


class Permissions(BaseModel):
  class Role(models.TextChoices):
    VIEWER = 0
    ADMIN = 1
    EDITOR = 3

  id = models.AutoField(auto_created=True, primary_key=True)
  role = models.IntegerField(default=0)
  organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

  class Meta:
    db_table = "permissions"


class Subjects(BaseModel):
  id = models.AutoField(auto_created=True, primary_key=True)
  name = models.CharField(max_length=50)

  class Meta:
    db_table = "subjects"


class Classrooms(BaseModel):
  class ClassroomStatus(models.TextChoices):
    SEEN_BY_TEACHER_ONLY = 0
    EDIT_BY_TEACHER_ONLY = 1
    SEEN_ONLY = 2
    NO_PERMISSION = 3

  id = models.AutoField(auto_created=True, primary_key=True)
  school_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
  subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
  student_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  schoolyear = models.DateField()
  status = models.IntegerField(default=0)

  class Meta:
    db_table = "classrooms"


class Tests(BaseModel):
  class TestType(models.TextChoices):
    OTHER = 0
    _1SCORE = 1
    _2SCORE = 2
    _3SCORE = 3

  id = models.AutoField(auto_created=True, primary_key=True)
  name = models.CharField(max_length=50)
  coefficient = models.IntegerField(default=0)
  classroom_id = models.ForeignKey(Classrooms, on_delete=models.CASCADE)

  class Meta:
    db_table = "tests"


class UserTests(BaseModel):
  class Qualification(models.TextChoices):
    EXCELLENT = 0
    GOOD = 1
    DONE = 2
    UNDONE = 3

  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
  score = models.FloatField()
  level = models.IntegerField(default=0)
  comments = models.TextField()

  class Meta:
    db_table = "user_tests"


class Notifications(BaseModel):
  id = models.AutoField(auto_created=True, primary_key=True)
  title = models.TextField(null=True)
  content = models.TextField(null=True)
  link_to = models.URLField(max_length=200)

  class Meta:
    db_table = "notifications"


class UserNotifications(BaseModel):
  class CreatedType(models.TextChoices):
    ORGANIZATION = 0
    USER = 1

  id = models.AutoField(auto_created=True, primary_key=True)
  notification_id = models.ForeignKey(Notifications, on_delete=models.CASCADE)
  created_by = models.IntegerField()
  to_user = models.ForeignKey(Users, on_delete=models.CASCADE)
  created_from = models.IntegerField(default=0)
  is_read = models.BooleanField(default=False)

  class Meta:
    db_table = "user_notifications"
