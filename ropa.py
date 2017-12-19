from ropa.gui import App

if __name__ == '__main__':
    app_name = 'ropa'

    w = App(app_name)
    w.resize(1200, 720)
    w.move(300, 300)

    w.show()
    w.quit()
