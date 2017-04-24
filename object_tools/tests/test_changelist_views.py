from django.contrib.auth.models import User
from django.test import TestCase

from object_tools import tools
from object_tools.tests.tools import TestTool, TestMediaTool


class ChangeListViewTestCase(TestCase):
    """
    TestCase for testing if tool is display in a model's changelist view.
    """
    def setUp(self):
        self.user = User.objects.create_superuser(username="testuser", password="password", email="testuser@example.com")
        self.client.login(username="testuser", password="password")

    def test_tool_is_rendered(self):
        tools.register(TestTool, User)
        tools.register(TestMediaTool, User)
        response = self.client.get("/admin/auth/user/")
        tool_html = '<li><a href="/object-tools/auth/user/test_tool/?"' \
                    ' title=""class="historylink">Test Tool</a></li>'
        self.assertContains(response, tool_html)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        tools._registry.clear()
