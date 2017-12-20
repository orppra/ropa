import backend  # noqa
from .gui import App  # noqa


def start(args):
    app_name = 'ropa'

    w = App(app_name, args)
    w.resize(1200, 720)
    w.move(300, 300)

    w.show()
    w.quit()
