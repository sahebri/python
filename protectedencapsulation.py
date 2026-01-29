class car:
    def __init__(self,brand,model,engine):
        self.brand=brand
        self._model=model
        self._engine=engine
    def _show_details(self):
        print(f"Brand:{self.brand},model:{self._model},engine:{self._engine}")
class Electriccar(car):
    def __init__(self,brand,model,b_cap):
        super() .__init__(brand,model,"Electric")
        self.b_cap=b_cap
    def show(self):
        self._show_details()
        print(f"battery:{self.b_cap}kwh")
tesla=Electriccar("Tesla","Model S",100)
tesla.show()