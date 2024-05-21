class Phone: 
    def __init__(self,brand,model_name,price):
        self._brand = brand
        self._model_name =  model_name
        self._price =  max(price,0)
        
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
    
    def __str__(self):
        return f"{self._brand}{self._model_name}"
    
    def discount(self):
        return self._price * 0.10
    
class SmartPhone(Phone): 
     def __init__(self,brand,model_name,price, ram, internal_memory, back_camera):  
        
        super().__init__(brand,model_name,price)  
        
        self.ram = ram
        self.internal_memory =  internal_memory
        self.back_camera = back_camera
        
     def discount(self):
        return self._price * 0.15
        
Moto =  Phone('Moto','G7',1000)
print(Moto)
Moto.make_a_call(232132)
print(f"Valor do {Moto._brand}{Moto._model_name} com desconto é {Moto.discount()}")
print(vars(Moto))

Iphone = SmartPhone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
Iphone.make_a_call(32142342)
print(f"Valor do {Iphone._brand}{Iphone._model_name} com desconto é {Iphone.discount()}")
print(vars(Iphone))
