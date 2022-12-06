from django.db import transaction
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions  # , generics, filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from goals.models.board import Board
from goals.models.goal import Goal
from goals.permissions import BoardPermissions
from goals.serializers.board import BoardSerializer


class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance: Board):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(
                status=Goal.Status.archived
            )
        return instance

# ??????????????????????????????????????????????????????????????????????
# class BoardListView(generics.ListAPIView):
#     model = Board
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = BoardSerializer
#     filter_backends = [
#         DjangoFilterBackend,
#         filters.OrderingFilter,
#         filters.SearchFilter,
#     ]
#     ordering_fields = ['limit', 'offset']
#     ordering = ['limit', 'offset']
#     search_fields = ['title']
#
#     def get_queryset(self):
#         return Board.objects.filter(user=self.request.user).exclude(status=Board.Status.archived)
