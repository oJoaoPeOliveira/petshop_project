from modelos.cachorro import Cachorro
from modelos.cliente import Cliente
from modelos.veterinario import Veterinario
from modelos.consulta import Consulta

def main():
	cachorro1 = Cachorro('Luffy', 0.8, 'Yorkshire')
	cachorro2 = Cachorro('Lu', 0.8, 'Yorkshire')
	cachorro3 = Cachorro('Luf', 0.8, 'Yorkshire')
	cliente = Cliente('João Pedro', '323200', '513232', '93293293')
	veterinario = Veterinario('Manu', '2039029', '32322', 'vet@gmail.com', 3000, '0001')
	
	cliente.adicionar_pet(cachorro1)
	cliente.adicionar_pet(cachorro2)
	cliente.adicionar_pet(cachorro3)
	
	nova_consulta = Consulta(cachorro1, cliente, veterinario, '22/11/2025', '10:00', '11:00', 100, 'Exame de rotina')
	print(nova_consulta)
	
if __name__ == '__main__':
	main()