import factory

from core.models import User
from goals.models.board import Board, BoardParticipant
from goals.models.category import GoalCategory
from goals.models.comment import GoalComment
from goals.models.goal import Goal


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = "password"


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("name")


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    title = factory.Faker("name")


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = factory.Faker("name")


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalComment

    text = "text comment"
