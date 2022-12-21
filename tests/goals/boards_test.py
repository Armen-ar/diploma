import json

import pytest
from django.urls import reverse

from goals.serializers.board import BoardSerializer
from tests import factories


@pytest.mark.django_db
def test_create(auth_client):
    response = auth_client.post(reverse("board_create"),
                                data={"title": "test_board"})
    expected_response = {"id": response.data["id"],
                         "created": response.data.get("created"),
                         "updated": response.data.get("updated"),
                         "title": "test_board",
                         "is_deleted": False, }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_list(auth_client, new_user):
    count = 5
    boards = factories.BoardFactory.create_batch(count)
    for board in boards:
        factories.ParticipantFactory.create(board=board, user=new_user)

    response = auth_client.get(f"{reverse('board_list')}?limit=" + str(count))

    expected_response = {"count": count,
                         "next": None,
                         "previous": None,
                         "results": BoardSerializer(instance=boards, many=True).data}

    response.data['results'].sort(key=lambda e: e['id'])

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve(auth_client, new_user, board, participant):
    response = auth_client.get(reverse('board_pk', args=[board.pk]))

    expected_response = BoardSerializer(instance=board).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_delete(auth_client, new_user, board, participant):
    response = auth_client.delete(reverse('board_pk', args=[board.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
def test_update(auth_client, new_user, board, participant):
    response = auth_client.put(reverse('board_pk', args=[board.pk]),
                               data=json.dumps({"title": "put test title", "participants": []}),
                               content_type="application/json")

    assert response.status_code == 200
    assert response.data.get('title') == "put test title"
