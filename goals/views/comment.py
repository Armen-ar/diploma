from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions

from goals.models.comment import GoalComment
from goals.serializers.comment import GoalCommentSerializer, GoalCommentCreateSerializer


class GoalCommentCreateView(generics.CreateAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentCreateSerializer


class GoalCommentListView(generics.ListAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['goal']
    ordering = ['-created']

    def get_queryset(self):
        return GoalComment.objects.filter(user=self.request.user)


class GoalCommentView(generics.RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GoalComment.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance
