from modelos.cachorro import Cachorro
from modelos.cliente import Cliente

def main():
	cachorro1 = Cachorro('Luffy', 0.8, 'Yorkshire')
	cachorro2 = Cachorro('Lu', 0.8, 'Yorkshire')
	cachorro3 = Cachorro('Luf', 0.8, 'Yorkshire')
	cliente = Cliente('João Pedro', 323200, 513232, 93293293)
	
	cliente.adicionar_pet(cachorro1)
	cliente.adicionar_pet(cachorro2)
	cliente.adicionar_pet(cachorro3)
	print(cliente)
	
	print('-------------------')
	
if __name__ == '__main__':
	main()