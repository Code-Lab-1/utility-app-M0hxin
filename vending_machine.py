print("Welcome to the vending machine")
print( "ITEMS             PRICE      CODE" )
A=("fanta             $1          11")
B=("Aquafina          $1          12")
C=("Masafi            $1          13")
D=("Pepsi             $3          14")
E=("Arwa              $3          15")
F=("Coca cola         $3          16")
G=("Fruit jelly       $1          17")
H=("Jelly beans       $1          18")
I=("Soda jelly        $1          19")
J=("Sour jelly        $1          20")
K=("Apple juice       $2          21")
L=("Mango juice       $2          22")
M=("Grape juice       $2          23")
N=("Mix fruit juice   $2          24")
O=("Lays(Salt)        $2          25")
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(I)
print(J)
print(K)
print(L)
print(M)
print(N)
print(O)
x=str(input("Enter the code="))
if x=="11":
    print("You have choose fanta")
    y=float(input("pay the amount="))
    fanta = 1 
    if y > fanta:
        print("take your change with ur selected item= ",y - fanta)
    elif y<fanta:
        print("no enough money")
        print("ur money is refunded")
    elif y==fanta:
        print("here ur pepsi")

elif x == "12":
    print("u have choose Aquafina")
    y=float(input("pay the amount="))
    Aquafina = 1
    if y > Aquafina:
        print("take your change with ur selected item= ",y - Aquafina)
    elif y<Aquafina:
        print("no enough money")
        print("ur money is refunded")
    elif y==Aquafina:
        print("here ur Aquafina")

elif x == "13":
    print("u have choose Masafi")
    y=float(input("pay the amount="))
    Masafi = 1
    if y > Masafi:
        print("take your change with ur selected item= ",y - Masafi)
    elif y<Masafi:
        print("no enough money")
        print("ur money is refunded")
    elif y==Masafi:
        print("here ur Masafi")

elif x == "14":
    print("u have choose Pepsi")
    y=float(input("pay the amount="))
    Pepsi = 3
    if y > Pepsi:
        print("take your change with ur selected item= ",y - Pepsi)
    elif y<Pepsi:
        print("no enough money")
        print("ur money is refunded")
    elif y==Pepsi:
      print("here ur Pepsi")

elif x == "15":
  print("u have choose Arwa")
  y=float(input("pay the amount="))
  Arwa = 3
  if y > Arwa:
      print("take your change with ur selected item= ",y - Arwa)
  elif y<Arwa:
      print("no enough money")
      print("ur money is refunded")
  elif y==Arwa:
      print("here ur Pepsi")

elif x == "16":
  print("u have choose Coca cola ")
  y=float(input("pay the amount="))
  Cocacola = 3
  if y > Cocacola:
      print("take your change with ur selected item= ",y - Cocacola)
  elif y<Cocacola:
      print("no enough money")
      print("ur money is refunded")
  elif y==Cocacola:
      print("here ur Coca cola")

elif x == "17":
  print("u have choose Fruit jelly ")
  y=float(input("pay the amount="))
  Fruitjelly = 1
  if y > Fruitjelly:
      print("take your change with ur selected item= ",y - Fruitjelly)
  elif y<Fruitjelly:
      print("no enough money")
      print("ur money is refunded")
  elif y==Fruitjelly:
      print("here ur Fruit jelly")

elif x == "18":
  print("u have choose Jelly beans ")
  y=float(input("pay the amount="))
  Jellybeans = 1
  if y > Jellybeans:
      print("take your change with ur selected item= ",y - Jellybeans)
  elif y<Jellybeans:
      print("no enough money")
      print("ur money is refunded")
  elif y==Jellybeans:
      print("here ur Fruit jelly")

elif x == "19":
  print("u have choose Soda jelly ")
  y=float(input("pay the amount="))
  Sodajelly = 1
  if y > Sodajelly:
      print("take your change with ur selected item= ",y - Sodajelly)
  elif y<Sodajelly:
      print("no enough money")
      print("ur money is refunded")
  elif y==Sodajelly:
      print("here ur Soda jelly")

elif x == "20":
  print("u have choose Sour jelly")
  y=float(input("pay the amount="))
  Sourjelly  = 1
  if y > Sourjelly:
      print("take your change with ur selected item= ",y - Sourjelly)
  elif y<Sourjelly:
      print("no enough money")
      print("ur money is refunded")
  elif y==Sourjelly:
      print("here ur Sour jelly")

elif x == "21":
  print("u have choose Apple juice")
  y=float(input("pay the amount="))
  Applejuice   = 2
  if y > Applejuice:
      print("take your change with ur selected item= ",y - Applejuice)
  elif y<Applejuice:
      print("no enough money")
      print("ur money is refunded")
  elif y==Applejuice:
      print("here ur Apple juice ")

elif x == "22":
  print("u have choose Mango juice")
  y=float(input("pay the amount="))
  Mangojuice = 2
  if y > Mangojuice:
      print("take your change with ur selected item= ",y - Mangojuice)
  elif y<Mangojuice:
      print("no enough money")
      print("ur money is refunded")
  elif y==Mangojuice:
      print("here ur Mango juice")

elif x == "23":
  print("u have choose Grape juice")
  y=float(input("pay the amount="))
  Grapejuice = 2
  if y > Grapejuice:
      print("take your change with ur selected item= ",y - Grapejuice)
  elif y<Grapejuice:
      print("no enough money")
      print("ur money is refunded")
  elif y==Grapejuice:
      print("here ur Grape juice")

elif x == "24":
  print("u have choose Mix fruit juice")
  y=float(input("pay the amount="))
  Mixfruitjuice = 2
  if y > Mixfruitjuice:
      print("take your change with ur selected item= ",y - Mixfruitjuice)
  elif y<Mixfruitjuice:
      print("no enough money")
      print("ur money is refunded")
  elif y==Mixfruitjuice:
      print("here ur Mix fruit juice")

elif x == "25":
  print("u have choose Lays(Salt)")
  y=float(input("pay the amount="))
  LaysSalt = 2
  if y > LaysSalt:
      print("take your change with ur selected item= ",y - LaysSalt)
  elif y<LaysSalt:
      print("no enough money")
      print("ur money is refunded")
  elif y==LaysSalt:
      print("here ur Lays(Salt)")

while True:
    z=str(input(" buy something more yes/no="))
    if z=='no':
        print("your item are processing... please wait a moment")
        break
    elif z=='yes':
       x=str(input("input code to buy "))

    if x=="11":
        print("u have choose fanta")
        y=float(input("pay the amount="))
        fanta =1
        if y > fanta:
          print("your change remaining is= ",y- fanta)
        elif y<fanta:
          print("no enough money")
        elif y==fanta:
          print("here ur fanta")

    if x=="12":
        print("u have choose Aquafina")
        y=float(input("pay the amount="))
        Aquafina =1
        if y > Aquafina:
          print("your change remaining is= ",y- Aquafina)
        elif y<Aquafina:
          print("no enough money")
        elif y==Aquafina:
          print("here ur Aquafina")

    if x=="13":
        print("u have choose Masafi")
        y=float(input("pay the amount="))
        Masafi =1
        if y > Masafi:
          print("your change remaining is= ",y- Masafi)
        elif y<Masafi:
          print("no enough money")
        elif y==Masafi:
          print("here ur Masafi")

    if x=="14":
        print("u have choose Pepsi")
        y=float(input("pay the amount="))
        Pepsi =3
        if y > Pepsi:
          print("your change remaining is= ",y- Pepsi)
        elif y<Pepsi:
          print("no enough Pepsi")
        elif y==Pepsi:
          print("here ur Pepsi")

    if x=="15":
        print("u have choose Arwa")
        y=float(input("pay the amount="))
        Arwa =3
        if y > Arwa :
          print("your change remaining is= ",y- Arwa)
        elif y<Arwa :
          print("no enough Arwa")
        elif y==Arwa :
          print("here ur Arwa")

    if x=="16":
        print("u have choose Coca cola")
        y=float(input("pay the amount="))
        Cocacola =3
        if y > Cocacola :
          print("your change remaining is= ",y- Cocacola)
        elif y<Cocacola :
          print("no enough Cocacola")
        elif y==Cocacola :
          print("here ur Coca cola")

    if x=="17":
        print("u have choose Fruit jelly")
        y=float(input("pay the amount="))
        Fruitjelly =1
        if y > Fruitjelly :
          print("your change remaining is= ",y- Fruitjelly)
        elif y<Fruitjelly :
          print("no enough Fruitjelly")
        elif y==Fruitjelly :
          print("here ur Fruit jelly")

    if x=="18":
        print("u have choose Jelly beans ")
        y=float(input("pay the amount="))
        Jellybeans  =1
        if y > Jellybeans:
          print("your change remaining is= ",y- Jellybeans)
        elif y<Jellybeans:
          print("no enough Jellybeans")
        elif y==Jellybeans :
          print("here ur Fruit jelly")

    if x=="19":
        print("u have choose Soda jelly")
        y=float(input("pay the amount="))
        Sodajelly =1
        if y > Sodajelly:
          print("your change remaining is= ",y- Sodajelly)
        elif y<Sodajelly:
          print("no enough Sodajelly")
        elif y==Sodajelly:
          print("here ur Soda jelly")

    if x=="20":
        print("u have choose Sour jelly")
        y=float(input("pay the amount="))
        Sourjelly =1
        if y > Sourjelly:
          print("your change remaining is= ",y- Sourjelly)
        elif y<Sourjelly:
          print("no enough Sourjelly")
        elif y==Sodajelly:
          print("here ur Sour jelly")

    if x=="21":
        print("u have choose Apple juice")
        y=float(input("pay the amount="))
        Applejuice  =2
        if y > Applejuice:
          print("your change remaining is= ",y- Applejuice)
        elif y<Applejuice:
          print("no enough Applejuice")
        elif y==Applejuice:
          print("here ur Applejuice")

    if x=="22":
        print("u have choose Mango juice")
        y=float(input("pay the amount="))
        Mangojuice =2
        if y > Mangojuice:
          print("your change remaining is= ",y- Mangojuice)
        elif y<Mangojuice:
          print("no enough Mangojuice")
        elif y==Mangojuice:
          print("here ur Mango juice")

    if x=="23":
        print("u have choose Grape juice")
        y=float(input("pay the amount="))
        Grapejuice =2
        if y > Grapejuice:
          print("your change remaining is= ",y- Grapejuice)
        elif y<Grapejuice:
          print("no enough Grapejuice")
        elif y==Grapejuice:
          print("here ur Grape juice")

    if x=="24":
        print("u have choose Mix fruit juice")
        y=float(input("pay the amount="))
        Mixfruitjuice =2
        if y > Mixfruitjuice:
          print("your change remaining is= ",y- Mixfruitjuice)
        elif y<Mixfruitjuice:
          print("no enough Mixfruitjuice")
        elif y==Mixfruitjuice:
          print("here ur Mix fruit juice")

    if x=="25":
        print("u have choose Mix Lays(Salt)")
        y=float(input("pay the amount="))
        LaysSalt =2
        if y > LaysSalt:
          print("your change remaining is= ",y- LaysSalt)
        elif y<LaysSalt:
          print("no enough LaysSalt")
        elif y==LaysSalt:
          print("here ur Lays(Salt)")

print("collect your items")
print("thank you.")