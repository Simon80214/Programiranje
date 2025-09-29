print("izbornik za kalkulaor")
print("---------------------")
print("1.Izračun napona")
print("2.Izračun otpora")
print("3. Izračun jakosti struje")
print("4.Izračun ukupnog srijskog otpora")
print("5.Izračun ukupnog paralenog otpora")
print("---------------------")
opcija=int(input(print("Izaberite operaciju (1 / 2 / 3 / 4 / 5): ")))
#sruktura grananja
if opcija == 1:
    print("Iračun napona struje")
    jakost=int(input("upiši jakost struje"))
    otpor=int(input("upiši otpor0"))
    napon=jakost*otpor
    print(f"Napon struje je:{napon}")
elif opcija ==2:
    print("izračun otpora struje")
    napon=int(input("upiši napon"))
    jakost=int(input("upiši jakost struje"))
    otpor=napon/jakost
    print(f"Otpor je: {otpor} ohm")
elif opcija == 3:
    print("Izračun jakosti struje:")
    napon= int(input("upiši napon"))
    otpor= int(input("upiši otpor"))
    jakost=napon/otpor
    print(f"Jakost struje je: {jakost} A")
elif opcija == 4:
    print("izračun serijskog otpora")
    otpor1= int(input("upiši R1"))
    otpor2=int(input("upiši R2"))
    Uotpor=otpor1+otpor2
    print(f"Izračun serijskog otpora {Uotpor} ")
elif opcija == 4:
    print("Izračun paralelnog otpora")
    R1= int(input("upiši R1"))
    R2= int(input("upiši R2"))
    R=(R1*R2)/(R1+R2)
    print(f"Izračun paralelnog otpora {R}")
else:
    print("POGREŠAN UNOS")

