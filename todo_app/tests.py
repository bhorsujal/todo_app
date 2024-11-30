from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoAppTests(TestCase):
    def setUp(self):
        self.task1 = Todo.objects.create(title="Task 1", description="Description 1")
        self.task2 = Todo.objects.create(title="Task 2", description="Description 2", isCompleted=False)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
        self.assertFalse(self.task1.isCompleted)

    def test_create_task_view(self):
        response = self.client.post(reverse('todo-list'), {'title': 'New Task', 'description': 'New Task Description'})
        self.assertEqual(response.status_code, 302) # should redirect to home
        self.assertEqual(Todo.objects.count(), 3)
        self.assertTrue(Todo.objects.filter(title='New Task').exists())

    def test_update_task_view(self):
        response = self.client.post(reverse('todo-update', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.isCompleted)

    def test_delete_task_view(self):
        response = self.client.post(reverse('todo-delete', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=self.task1.id).exists())

    def test_delete_all_tasks_view(self):
        response = self.client.post(reverse('todo-delete-all'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)

    def test_update_task_details_view(self):
        response = self.client.post(reverse('todo-update-details', kwargs={'pk': self.task1.pk}), {
            'title': 'Updated Title',
            'description': 'Updated Description'
        })
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Title')
        self.assertEqual(self.task1.description, 'Updated Description')