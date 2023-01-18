import csv

Shipping_List = {}

L306ER = {'L306ER':'AB'}
AI8AB = {'5069-IF8':'AB'}
B1 = {'772101':'Pilz'}
Safety_Net = {'772122':'Pilz'}
DI16P = {'772140':'Pilz'}
DI8DO4 = {'772142':'Pilz'}
DI4DO4R = {'772143':'Pilz'}
Scrw_Ter = {'750017':'Pilz'}
Scrw_Ter1 = {'793538':'Pilz'}
Scrw_Ter2 = {'750004':'Pilz'}
OB16 = {'5069-OB16':'AB'}
OF4 = {'5069-OF4':'AB'}
IB16 = {'5069-IB16':'AB'}


Shipping_List.update(L306ER)
Shipping_List.update(AI8AB)
Shipping_List.update(B1)
Shipping_List.update(Safety_Net)
Shipping_List.update(DI16P)
Shipping_List.update(DI8DO4)
Shipping_List.update(DI4DO4R)
Shipping_List.update(Scrw_Ter)
Shipping_List.update(Scrw_Ter1)
Shipping_List.update(Scrw_Ter2)
Shipping_List.update(OB16)
Shipping_List.update(OF4)
Shipping_List.update(IB16)

list = list(Shipping_List.keys())

for i in range(1):
    for q in range(0,4):
        list.append('772122')
        list.append('5069-OB16')
    for w in range(0,3):
        list.append('750004')
    for e in range(0,2):
        list.append('772143')
        list.append('L306ER')


counts = {}
for item in set(list):
    counts[item] = list.count(item)

print("The items to be shipped are as follows:", '\n')

for item in list:
    print(item, '\n')

for key, value in counts.items():
    print(f"The amount of {key} units that were shipped is {value}")

with open('shipping_list.csv', 'w', newline='') as csvfile:
    fieldnames = ['Item', 'Quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for key, value in counts.items():
        writer.writerow({'Item': key, 'Quantity': value})