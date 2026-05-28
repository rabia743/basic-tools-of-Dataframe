import pandas as pd
data = {"Name":["Ali","Ahmad","Abbas","Raza","Zafar","Akram"],
        "Subject":["CS","SE","CS","SE","CS","SE"],
        "city":["Karachi","Lahore","Islamabad","Peshawar","Quetta","Faisalabad"]}
s = pd.DataFrame(data)
print(s.head(6)) # isse se hum 6 row print ker sektha ha
print(s.shape) # isse se hum row aur column ki total number print ker sektha ha
print(s.info()) # isse se hum data ke baare me information milti ha jaise ki data type aur null
print(s.tail(2)) # isse se hum last 2 row print ker sektha ha
print(s.describe()) # isse se hum data ke baare me statistical information milti ha
