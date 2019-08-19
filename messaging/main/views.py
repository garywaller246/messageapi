from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from . models import Message
from . serializers import MessageSerializer, MessageOutputSerializer


# Create your views here.

class MessagePageView(APIView):
  permission_classes = (permissions.IsAuthenticated,)


  def list(self, request):
    messages = Message.objects.filter(receiver=request.user).all()
    serializer  = MessageOutputSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


  def get(self, request, pk=None):
    if pk is None:
      return self.list(request)

    message = Message.objects.get(pk=pk)
    serializer = MessageOutputSerializer(message)

    if message.receiver == request.user:
      message.read = True
      message.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.user == message.sender:
      return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_403_FORBIDDEN)


  def delete(self, request, pk):
    if pk is None:
      return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    message = Message.objects.get(pk=pk)
    
    if request.user not in [message.sender, message.receiver]:
      return Response(serializer.error_messages, status=status.HTTP_403_FORBIDDEN)

    message.delete()
    return Response(status=status.HTTP_200_OK)


  def post(self, request, receiver_pk):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid(raise_exception=ValueError):
      message = serializer.create(validated_data=request.data, sender=request.user, receiver_pk=receiver_pk)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
