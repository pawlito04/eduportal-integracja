from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Course, Module, Lesson, Enrollment


class CourseViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.course = Course.objects.create(
            title="Django Course",
            description="Learn Django",
            level="beginner",
        )
        self.module = Module.objects.create(
            course=self.course,
            title="Intro module",
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            title="Lesson 1",
            content="Lesson content",
        )

    def test_course_list_view_returns_200(self):
        response = self.client.get(reverse("courses:course_list"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_course_detail_view_returns_200(self):
        response = self.client.get(
            reverse("courses:course_detail", args=[self.course.pk]),
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_enroll_course_requires_login(self):
        response = self.client.get(
            reverse("courses:enroll_course", args=[self.course.pk]),
            follow=False,
        )
        self.assertIn(response.status_code, [301, 302])

    def test_logged_user_can_enroll_in_course(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(
            reverse("courses:enroll_course", args=[self.course.pk]),
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Enrollment.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_lesson_detail_redirects_if_user_not_enrolled(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(
            reverse("courses:lesson_detail", args=[self.lesson.pk]),
            follow=False,
        )

        self.assertIn(response.status_code, [301, 302])
