flag = False
serials = []
while flag == False:
  eingabe = input("Seriennummern eingeben (0 für ende): ") 
  if int(eingabe) == 0:
    flag = True
  else:
    serials.append(int(eingabe.strip()))
m = max(serials)
s = m + m/len(serials) - 1 
print("Geschätzte Größe der Serie: " + str(int(s)))