
n1 = int(input("Coloque o primeiro numero: "))
n2 = int(input("Coloque o segundo numero: "))

#Contas adições
add = n1 + n2 

add2 = 20 + 30
adicao = 200 + 30

add4 = 200 + 300
add5 = 30 + 24

#Contas subtrações 
sub = n1 - n2

sub1 = 30 - 20 
sub2 = 60 - 30

#Contas multiplicações
mult = n1 * n2
mult1 = 49 * 7
mult2 = 21 * 3

#Conta divisões
div = 42 / 2
div2 = 80 / 5

division2 = 30 / 3
division = n1 / n2

#Conta extras
conta = (((n1 * 2) * 10) / 2) ** 2  

outra_conta = (((n2 * 3) * 5) / 3) ** 3
conta2 = ((((10 * 4) * 2) / 4)) ** 3


print("\n===== Adições =====\n")
print(f"Resultado de {n1} + {n2} = {add}")
print(f"Outras adições\n20 + 30 = {add2}\n200 + 30 = {adicao}")

print("\n===== Subtrações =====\n")
print(f"Resultado de {n1} - {n2} = {sub}")
print(f"Resultado de 30 - 20  = {sub1}")
print(f"Resultado de 60 - 30  = {sub2}")

print("\n===== Divisões =====\n")
print(f"Resultado de {n1} / {n2} = {division}")
print(f"Resultado de 30 / 3 = {division2}")
print(f"Outras divisões\n40 / 2 = {div}\n50 / 3 = {div2}")

print("\n===== Multiplicações =====\n")
print(f"Resultado de {n1} x {n2} = {mult}")
print(f"Resultado de 49 x 7  = {mult1}")
print(f"Resultado de 21 x 3  = {mult2}")

print("\n===== Conta extras =====\n")
print(f"(((n1 x 2) x 10) / 2)^2 = ", conta)

