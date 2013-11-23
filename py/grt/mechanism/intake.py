from threading import Timer


class Intake:

    t = Timer(0, lambda: None)  # init with null timer

    def __init__(self, joystick, epmotor, beltsmotor):

        self.joystick = joystick
        self.epmotor = epmotor
        self.beltsmotor = beltsmotor

        self.joystick.add_listener(self.intake_listener)

    def intake_listener(self, source, id, datum):
        if id == 'button2':
            if datum:
                self.t.cancel()
                self.epmotor.Set(1)
                self.beltsmotor.Set(-1)
                self.t = Timer(5, lambda: self.beltsmotor.Set(0))
                self.t.start()
            else:
                self.epmotor.Set(0)
        elif id == 'button3':
            if datum:
                self.t.cancel()
                self.epmotor.Set(-1)
                self.beltsmotor.Set(1)
                self.t = Timer(5, lambda: self.beltsmotor.Set(0))
                self.t.start()
            else:
                self.epmotor.Set(0)
