from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo

# Create your tests here.

class TodoAPITestCase(APITestCase):
    def setUp(self):
        self.todo1 = Todo.objects.create(title='Task 1', description='Description 1')
        self.todo2 = Todo.objects.create(title='Task 2', description='Description 2')

    def test_create_todo(self):
        url = reverse('todo-list')
        data = {'title': 'New Task', 'description': 'New Description'}
        response = self.client.post(url, data, format='json') # made one todo object
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 3) # at setup there were two objects

    def test_list_todos(self):
        url = reverse('todo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_todo(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo1.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_put_todo(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo2.pk})
        data = {'title': 'Updated Task 2', 'description': 'Updated Description 2', 'isCompleted': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo2.refresh_from_db()
        self.assertEqual(self.todo2.title, 'Updated Task 2')
        self.assertEqual(self.todo2.isCompleted, True)

    def test_patch_todo(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo2.pk})
        data = {'title': 'Updated Task 2 (Patch)'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo2.refresh_from_db()
        self.assertEqual(self.todo2.title, 'Updated Task 2 (Patch)')

    def test_delete_todo(self):
        url = reverse('todo-detail', kwargs={'pk': self.todo1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 1)

    def test_delete_all_todos(self):
        url = reverse('todo-delete-all')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)