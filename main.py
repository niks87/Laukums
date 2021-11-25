print('Programma pieprasa figūras elementus un aprēķina to lakumu.')
print('Nospiediet burtu:')
print('T   - ja figura trijstūris')
print('Tr  - ja figūra trapece')
print('P   - ja figūra paralelograms')
print('Ta  - ja figūra taisnstūris')
print('K   - ja figūra kvadrāts')
print('R   - ja figūra riņķis')
print('____________________')


PI = 3.14
r = float(input("Enter the radius of the circle: "))
area = PI * r * r
print("%.2f" %area)


side = int(input("Enter the side:"))
Area = side*side
print("Area of the square="+str(Area))
