from threading import Timer


class Intake:

    t = Timer(0, lambda: None)  # init with null timer

    def __init__(self,epmotor, beltsmotor):
        self.epmotor = epmotor
        self.beltsmotor = beltsmotor


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