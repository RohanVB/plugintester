import sublime_plugin


class HelloWorldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        view.insert(edit, view.sel()[0].begin(), "hello world")


def multfunc(a):
    return a*2
