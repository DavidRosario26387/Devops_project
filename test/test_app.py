import pytest
from app.backend.app import app, tasks

@pytest.fixture
def client():
    app.testing = True
    tasks.clear()  # clear tasks before each test
    return app.test_client()

def test_get_tasks_empty(client):
    rv = client.get("/tasks")
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_add_task(client):
    rv = client.post("/tasks", json={"task": "Test Task"})
    assert rv.status_code == 201
    assert rv.get_json()["task"] == "Test Task"

def test_update_task(client):
    rv_post = client.post("/tasks", json={"task": "Old Task"})
    task_id = rv_post.get_json()["id"]
    rv = client.put(f"/tasks/{task_id}", json={"task": "Updated Task"})
    assert rv.status_code == 200
    assert rv.get_json()["task"] == "Updated Task"

def test_delete_task(client):
    rv_post = client.post("/tasks", json={"task": "Task to delete"})
    task_id = rv_post.get_json()["id"]
    rv = client.delete(f"/tasks/{task_id}")
    assert rv.status_code == 200
    assert rv.get_json()["message"] == "Deleted"
