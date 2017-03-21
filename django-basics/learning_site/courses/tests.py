from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your tests here.
from .models import Course, Step

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(title="Python Regular Expressions", description="Learn to write regular expressions in Python.")
        now = timezone.now()
        #self.assertLess(course.created_at, now)
        self.assertEqual(course.created_at, now)

    def test_step_creation(self):
        course = Course.objects.create(title="Python Regular Expressions Course", description="Learn to write regular expressions in Python.")
        step = Step.objects.create(title="Python Regular Expressions Step", description="Learn to write regular expressions in Python.", course=course)
        now = timezone.now()
        self.assertLess(course.created_at, now)

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title="Python Testing", description="Learn to write unit tests in Python")
        self.course2 = Course.objects.create(title="Django Basics", description="Learn all about Django")
        self.step = Step.objects.create(title="View Tests", description="Learn about them here", course=self.course)
    
    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={'pk', self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])