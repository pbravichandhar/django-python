from rest_framework_mongoengine import serializers

from .models import Poll

class PollSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Poll
        fields = '__all__'