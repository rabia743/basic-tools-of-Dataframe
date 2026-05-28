import pandas as pd
data = {"Name":["Ali","Ahmad","Abbas","Raza","Zafar","Akram"],
        "Subject":["CS","SE","CS","SE","CS","SE"],
        "city":["Karachi","Lahore","Islamabad","Peshawar","Quetta","Faisalabad"]}
s = pd.DataFrame(data)
print(s.head(3)) 
print(s.shape)
print(s.info())
print(s.tail(2))
print(s.describe()) 
