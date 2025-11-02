from modelos.cliente import Cliente

def main():
	cliente = Cliente('João Pedro', '00000000', '17/07/1999', '93000000', 'Luffy')
	cliente = Cliente('João Pedro', '00000001', '17/07/1999', '93000000', 'Barry')
	Cliente.listar_clientes()
	
if __name__ == '__main__':
	main()