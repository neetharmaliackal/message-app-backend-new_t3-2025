


from rest_framework import status
from rest_framework.response import Response

from message.models import Message
from rest_framework.decorators import api_view

from message.serializers import MessageSerializer


@api_view(['POST'])
def send_message(request):
    message_serializer = MessageSerializer(data=request.data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response({'message': 'Message sent successfully'},
                        status=status.HTTP_201_CREATED)
    return None
