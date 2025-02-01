from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    status = serializers.ChoiceField(choices=[('user', 'user'), ('employee', 'employee')], required=True)
    image = serializers.ImageField(required=False)
    mobile_no = serializers.CharField(max_length=12, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'status', 'image', 'mobile_no']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        status = self.validated_data['status']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError({'error': "Passwords don't match"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_active = False  # Activate after email confirmation
        user.save()

        if status == 'employee':
            image = self.validated_data.get('image', 'employee/images/default_image.jpg')
            mobile_no = self.validated_data.get('mobile_no', '0000000000')

            employee = Employee(user=user, image=image, mobile_no=mobile_no,status=status)
            employee.save() 

        return user


class EmployeeLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
