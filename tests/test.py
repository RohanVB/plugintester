import sublime
import sys
from unittest import TestCase

version = sublime.version()

class TestHelloWorld(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def setText(self, string):
        self.view.run_command("insert", {"characters": string})

    def getRow(self, row):
        return self.view.substr(self.view.line(self.view.text_point(row, 0)))

    if version >= '3000':
        def test_hello_world_st3(self):
            self.view.run_command("hello_world")
            first_row = self.getRow(0)
            self.assertEqual(first_row, "hello world")

    def test_hello_world(self):
        self.setText("new ")
        self.view.run_command("hello_world")
        first_row = self.getRow(0)
        self.assertEqual(first_row, "new hello world")


# since it uses versions in K's
if version < '3000':
    # sublimetext2
    helloworld = sys.modules["helloworld"]
else:
    # sublimetext3
    helloworld = sys.modules["PluginTester.helloworld"]


class TestFunctions(TestCase):

    def test_multfunc(self):
        a = helloworld.multfunc(2)
        self.assertEqual(a, 4)
