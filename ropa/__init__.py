import backend  # noqa
from .gui import App  # noqa


def start(args, file=None, load=None):
    app_name = 'ropa'

    w = App(app_name, args, file, load)
    w.resize(1200, 720)
    w.move(300, 300)

    w.show()
    w.quit()
