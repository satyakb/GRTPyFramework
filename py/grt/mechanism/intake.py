from threading import Timer


class Intake:

    t = Timer(0, lambda: None)  # init with null timer

    def __init__(self, joystick, epmotor, beltsmotor):

        self.joystick = joystick
        self.epmotor = epmotor
        self.beltsmotor = beltsmotor
        self.joystick.add_listener(self.intake_listener)


    def startpickup(self):
        self.t.cancel()
        self.epmotor.Set(1)
        self.beltsmotor.Set(-1)

    def endpickup(self):
        self.epmotor.Set(0)
        self.t = Timer(5, lambda: self.beltsmotor.Set(0))
        self.t.start()

    def kickoutfrisbees(self):
        self.t.cancel()
        self.epmotor.Set(-1)
        self.beltsmotor.Set(1)

    def stopkickoutfisbees(self):
        self.epmotor.Set(0)
        self.t = Timer(5, lambda: self.beltsmotor.Set(0))
        self.t.start()


    def intake_listener(self, source, id, datum):
        if id == 'button2':
            if datum:
                self.t.cancel()
                self.epmotor.Set(1)
                self.beltsmotor.Set(-1)
            else:
                self.epmotor.Set(0)
                self.t = Timer(5, lambda: self.beltsmotor.Set(0))
                self.t.start()

        elif id == 'button3':
            if datum:
                self.t.cancel()
                self.epmotor.Set(-1)
                self.beltsmotor.Set(1)

            else:
                self.epmotor.Set(0)
                self.t = Timer(5, lambda: self.beltsmotor.Set(0))
                self.t.start()
