from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# get_user_model is used to reference our active User and TestCase.
from .models import Post
# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample ticket')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        # Tests to see if our homepage returns a 200 for its status code.
        self.assertEqual(response.status_code, 200)
        # Tests to see if the response has the body text.
        self.assertContains(response, 'Nice body content')
        # Tests to see if our homepage uses the correct html file.
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        # It's good practice tot est that something does or doesn't exist.
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code, 200)
        # Will return a 301 without the APPEND_SLASH variable in settings.py set to False, Django by default sets it
        # to true.
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    # Status code 302 is a redirect

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
