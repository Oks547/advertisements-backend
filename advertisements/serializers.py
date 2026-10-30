from rest_framework import serializers
from .models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator', 'status', 'created_at']
        read_only_fields = ['creator', 'created_at']

    def validate(self, data):
        # Проверяем лимит только при создании нового объявления
        if not self.instance:
            request = self.context.get('request')
            if request and request.user.is_authenticated:
                open_count = Advertisement.objects.filter(creator=request.user, status='OPEN').count()
                if open_count >= 10:
                    raise serializers.ValidationError("У вас не может быть больше 10 открытых объявлений.")
        return data