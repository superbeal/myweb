from django.contrib.auth.models import User


for number in range(1, 27):
    user = User.objects.create_user('number', 'no@qq.com', 'number')
    user.is_staff = True
    user.save()