import pytest
import requests


# In terminal, run 'pytest tests.py -v' to run the tests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []


def test_create_task():
    new_data = {
        "title": "Task 1",
        "description": "Description of the task"
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_data)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "id" in response.json()
    tasks.append(response.json()['id'])


def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        assert task_id == response.json()['id']


def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "title": "Task 1 updated",
            "description": "Description of the task updated",
            "completed": True
        }
        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
        assert response.status_code == 200
        assert "message" in response.json()

        # New requisition to check if the task was updated
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        assert payload['title'] == response.json()['title']
        assert payload['description'] == response.json()['description']
        assert payload['completed'] == response.json()['completed']


def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        assert "message" in response.json()

        # New requisition to check if the task was deleted
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404
        assert "message" in response.json()
        assert "Task not found" == response.json()['message']