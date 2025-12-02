from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Country, Tour, Booking
from .serializers import CountrySerializer, TourSerializer, BookingSerializer, UserSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.select_related('country').filter(is_active=True)
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()  # ← обязательно!

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()  # ← убирает жёлтые ошибки
        return Booking.objects.filter(user=self.request.user).select_related('tour__country')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Регистрация
from rest_framework.views import APIView
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')

        if not username or not password:
            return Response({"error": "Нужны username и password"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Пользователь уже есть"}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"id": user.id, "username": user.username}, status=201)