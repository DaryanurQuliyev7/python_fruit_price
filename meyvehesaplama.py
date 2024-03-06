while True:
 meyve = input("Hansi Meyveni Isteyirsiz? ")
 kilo = 0
 if meyve ==("banan"):
      kilo = int(input("Nece Kilo Banan Isteyirsiz? "))
      print(kilo*5,"Azn pul odeyeceksiniz. ")

 elif meyve ==("alma"):
     renk = input("Hansi reng alma isteyirsiz? ")
     if renk == ("qirmizi"):
         kilo = int(input("Nece Kilo Qirmizi Alma Isteyirsiz?"))

     elif renk ==("sarı"):
         kilo = int(input("Nece Kilo Sari Alma Isteyirsiz?"))

     elif renk ==("Yasil"):
         kilo = int(input("Nece kilo yasil alma isteyirsiz??"))
         
     else:
         print("Sadece sarı, qırmızı ya da yaşil renk alma var.")

     print(kilo*2,"Azn pul ödeyeceksiniz.")

 elif meyve == ("üzüm"):
     renk = input("Hansi renk üzüm isteyirsiz? ")
     if renk == ("qara"):
        kilo = int(input("Nece kilo qara uzum isteyirsiz "))
        print(kilo*3,"Azn pul odeyeceksiz.")
     elif renk ==("yasil"):
        kilo = int(input("Nece kilo yasil uzum isteyirsiz? "))
        print(kilo*3.5,"Azn odeyeceksiniz.")
     else:
       print("Sadece qara ve yasil renk uzum var.")
        
 else:
     print("Marketde sadece Banan,Uzum ve,Alma var ")