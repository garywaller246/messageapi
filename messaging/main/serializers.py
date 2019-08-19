from rest_framework import serializers
from . models import Message
from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):

  def create(self, validated_data, sender, receiver_pk):
    receiver = User.objects.get(pk=receiver_pk)
    message, created = Message.objects.get_or_create(**validated_data, sender=sender, receiver=receiver)
    return message


  def delete(self, pk):
    return Message.objects.filter(pk=pk).delete()


  class Meta:
    model = Message
    fields = ('content', 'subject')



class MessageOutputSerializer(serializers.ModelSerializer):
  sender = serializers.StringRelatedField()
  receiver = serializers.StringRelatedField()
  class Meta:
    model = Message
    fields = '__all__'