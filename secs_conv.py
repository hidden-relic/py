def conversion(sec):
   sec_value = sec % (24 * 3600)
   hour_value = sec_value // 3600
   sec_value %= 3600
   min = sec_value // 60
   sec_value %= 60
   print(str(hour_value)+':'+str(min)+':'+str(sec_value))
    
sec = (65*60)+27
conversion(sec)
