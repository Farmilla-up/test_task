from django.test import TestCase
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_task_crud_flow():
    """Тест CRUD операций для Task"""
    client = APIClient()

    # CREATE
    payload = {
        "title": "Тестовая задача",
        "description": "Описание для теста",
        "status": "created",
    }
    response = client.post("/tasks/", payload, format="json")
    assert response.status_code == 201
    task_id = response.json()["id"]

    # GET LIST
    response = client.get("/tasks/")
    assert response.status_code == 200
    ids = [t["id"] for t in response.json()]
    assert task_id in ids

    # GET SINGLE
    response = client.get(f"/tasks/{task_id}/")
    assert response.status_code == 200
    assert response.json()["title"] == "Тестовая задача"

    # UPDATE (PATCH)
    response = client.patch(f"/tasks/{task_id}/", {"status": "done"}, format="json")
    assert response.status_code == 200
    assert response.json()["status"] == "done"

    # DELETE
    response = client.delete(f"/tasks/{task_id}/")
    assert response.status_code == 204

    response = client.get(f"/tasks/{task_id}/")
    assert response.status_code == 404
