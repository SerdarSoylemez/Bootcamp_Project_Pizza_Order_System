# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:28:34 2023

@author: SerdarSoylemez
"""

import datetime
import csv

#Oluşturulan "Menu.txt" dosyası okundu
#pizza_menu ve sos_menu degiskenleri ayrıstırıldı.
with open('Menu.txt', 'r', encoding='utf-8') as f:
     lines = f.readlines()
     pizza_menu = [line.strip() for line in lines[1:5]]
     sos_menu =[line.strip() for line in lines[5:11]]
     
#Pizza üst sınıfı oluşturuldu.     
class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0

#KlassikPizza alt sınıfı Pizza sınıfından miras alarak oluşturuldu.Cost ve description degerleri pizzaya özel atandı.
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.cost = 50
        
    def get_description(self):
        return self.description
  
    def get_cost(self):
        return self.cost

#MargaritaPizza alt sınıfı Pizza sınıfından miras alarak oluşturuldu.Cost ve description degerleri pizzaya özel atandı.        
class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza"
        self.cost = 80
        
    def get_description(self):
        return self.description
      
    def get_cost(self):
        return self.cost

#TurkPizza alt sınıfı Pizza sınıfından miras alarak oluşturuldu.Cost ve description degerleri pizzaya özel atandı.        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza"
        self.cost = 70
        
    def get_description(self):
        return self.description
      
    def get_cost(self):
        return self.cost
 
#SadePizza alt sınıfı Pizza sınıfından miras alarak oluşturuldu.Cost ve description degerleri pizzaya özel atandı.       
class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
        self.cost = 60
        
    def get_description(self):
        return self.description
      
    def get_cost(self):
        return self.cost

#Bir Decorator sınıfı oluşturuldu.Decorator,burada tüm sos sınıflarının süper sınıfı olarak adlandırıldı.
class Decorator(Pizza):
    def __init__(self, component):
        
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost()
    
    def get_description(self):
        return self.component.get_description() 

#Zeytin sosuna ait sınıf oluşturuldu.Cost ve description degerleri sosa özel atandı. 
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin Soslu"
        self.cost = 5
        
    def get_description(self):
        return self.description + ' ' + self.component.get_description()
      
    def get_cost(self):
        return self.cost+self.component.get_cost()

#Mantarlar sosuna ait sınıf oluşturuldu.Cost ve description degerleri sosa özel atandı. 
class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantar Soslu"
        self.cost = 4
        
    def get_description(self):
        return self.description + ' ' + self.component.get_description()
      
    def get_cost(self):
        return self.cost+self.component.get_cost()

#Keci Peyniri sosuna ait sınıf oluşturuldu.Cost ve description degerleri sosa özel atandı. 
class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peyniri Soslu"
        self.cost = 7
        
    def get_description(self):
        return self.description + ' ' + self.component.get_description()
      
    def get_cost(self):
        return self.cost+self.component.get_cost()

#Et sosuna ait sınıf oluşturuldu.Cost ve description degerleri sosa özel atandı. 
class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Et Soslu"
        self.cost = 8
    def get_description(self):
        return self.description + ' ' + self.component.get_description()
      
    def get_cost(self):
        return self.cost+self.component.get_cost()

#Sogan sosuna ait sınıf oluşturuldu.Cost ve description degerleri sosa özel atandı. 
class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Soğan Soslu"
        self.cost = 3
        
    def get_description(self):
        return self.description + ' ' + self.component.get_description()
      
    def get_cost(self):
        return self.cost+self.component.get_cost()

#Mısır sosuna ait sınıf oluşturuldu.Cost ve description degerleri sosa özel atandı. 
class Misir(Decorator):
    def __init__(self, component):
      super().__init__(component)
      self.description = "Mısır Soslu"
      self.cost = 2
      
    def get_description(self):
        return self.description + ' ' + self.component.get_description()
    
    def get_cost(self):
        return self.cost+self.component.get_cost()
    
def pizzaSec():
        # Kullanıcının pizza tabanını seçmesi istendi.
        while True:
            for line in pizza_menu:
                print(line)
            pizza_choice = input("Lütfen bir pizza seçiniz:")
        # Seçilen pizza tabanına göre bir Pizza nesnesi oluşturuldu.
            if pizza_choice == "1":
                pizza = KlasikPizza()
                break
            elif pizza_choice == "2":
                pizza = MargaritaPizza()
                break
            elif pizza_choice == "3":
                pizza = TurkPizza()
                break
            elif pizza_choice == "4":
                pizza = SadePizza()
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin: ")
                continue
        return pizza 
def sosSec():
        pizza = pizzaSec()
        while True:
            for line in sos_menu:
                print(line)
        # Kullanıcının sosu seçmesini isteyin
            sauce_choice = int(input("Lütfen bir sos seçiniz:"))

        # Seçilen sos pizza üzerine eklendi.
            if sauce_choice == 11:
                pizza = Zeytin(pizza)
                break;
            elif sauce_choice == 12:
                pizza = Mantarlar(pizza)
                break;
            elif sauce_choice == 13:
                pizza = KeciPeyniri(pizza)
                break;
            elif sauce_choice == 14:
                pizza = Et(pizza)
                break;
            elif sauce_choice == 15:
                pizza = Sogan(pizza)
                break;
            elif sauce_choice == 16:
                pizza = Misir(pizza)
                break;
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                continue
        return pizza 
def main():
    
    
    pizza= sosSec()
    # Menü gösterildi.
    total_cost = pizza.get_cost()

    # Kullanıcının kişisel bilgilerini istendi.
    name = input("İsim: ")
    id_number = input("TC Kimlik Numarası: ")
    card_number = input("Kredi Kartı Numarası: ")
    card_password = input("Kredi Kartı Şifresi: ")

    # Sipariş verilerini dosyaya kaydedildi.
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Orders_Database.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([pizza.get_description(), name, id_number, card_number, total_cost, card_password,order_time])
    
    print("Siparişiniz alınmıştır.\nToplam tutar:", total_cost,"TL'dir.","\nAçıklama:",pizza.get_description())
    
    
if __name__ == "__main__":
    main()


