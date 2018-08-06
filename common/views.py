from django.contrib.auth.models import User, Group
from rest_framework.decorators import action

from base.views import BaseViewSet
from common.models import UserUtils
from .serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response


class UserViewSet(BaseViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(detail=False)
    def current(self, request):
        user = UserUtils.get_user_from_request(request)
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)


class GroupViewSet(BaseViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



