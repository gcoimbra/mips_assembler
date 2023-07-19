from Config import *
#fonte: Função binaryFormatComplement https://stackoverflow.com/questions/1604464/twos-complement-in-python?noredirect=1&lq=1

def isHex(value):
	"""Verifica se número é hex"""
	return (value[0:2] == "0x")


def isImmediate(instrucao):
	"""Verifica se a função é imediata"""
	return (instrucao[0] in cod_imediatos)

def isPseudo(instrucao):
	""" Detecta se a instrução é do tipo pseudo """
	return (instrucao[0] in cod_pseudo)

					   # return positive value as is

def binaryFormat(value,complement=False):
	""" Converte para uma string que contem 0s e 1s e representa o numero em complemento de dois"""
	if(value < 0):
		return "{0:b}".format(value)[1:]

	return "{0:b}".format(value)


def toStrBinary(string,offset,option=None):
	"""Converte numero para string binaria"""
	result = ""
	binary_aux_string = ""

	# Precisamos retornar um shamt
	if(option == "shamt"):
		binary_aux_string = binaryFormat(int(string))

	# Temos um lw ou sw, retorna registrador dentro do offset
	elif(option == "mem_reg"):
		binary_aux_string = binaryFormat(cod_registradores[string[-4:-1]])

	# Temos um lw ou sw, retorna offset que está antes do registrador
	elif(option == "mem_offset"):

		mem_offset = string[:-5]

		if(isHex(mem_offset)):
			binary_aux_string = binaryFormat(int(mem_offset,base=16))
		else:
			binary_aux_string = binaryFormat(int(mem_offset))

	# Precisamos retornar um endereço
	elif(option == "address"):
		if(isHex(string)):
			binary_aux_string = binaryFormat(int(string,base=16),True)
		else:
			binary_aux_string = binaryFormat(int(string),True)

	# Precisamos retornar uma funct
	elif(option == "funct"):
		binary_aux_string = binaryFormat(cod_instrucao[string][1])

	#Precisamos retornar um registrador
	elif(string in cod_registradores):
		binary_aux_string = binaryFormat(cod_registradores[string])

	#Precisamos retornar um opcode
	elif(string in cod_instrucao):

		binary_aux_string = binaryFormat(cod_instrucao[string][0])


	# Adiciona zeros até termos uma string do tamanho certo
	tam = len(binary_aux_string)
	while(tam < offset):
		result += "0"
		tam += 1

	result += binary_aux_string
	if(VERBOSE):
		print("toStrBinary(): string:",string,"aux string:",binary_aux_string,"result:",result,"result tam:",len(result))
	return result


def decImmediate(instrucao):
	"""Essa função lida com imediatos"""
	instrucao_binaria = ""
	# Opcode
	instrucao_binaria += toStrBinary(instrucao[0],6)

	# Reg
	if(instrucao[0] == "lw" or instrucao[0] == "sw"):
		instrucao_binaria += toStrBinary(instrucao[2],5,"mem_reg")
	else:
		instrucao_binaria += toStrBinary(instrucao[2],5)

	# Fonte
	instrucao_binaria += toStrBinary(instrucao[1],5)

	# Offset
	if(instrucao[0] == "lw" or instrucao[0] == "sw"):
		instrucao_binaria += toStrBinary(instrucao[2],16,"mem_offset")
	else:
		instrucao_binaria += toStrBinary(instrucao[3],16,"address")

	#'\n' maroto
	instrucao_binaria += '\n'

	if(VERBOSE):
		print("decImmediate():","".join(instrucao),"\n",instrucao_binaria,len(instrucao_binaria)-1)

	return instrucao_binaria


def decRegister(instrucao):
	"""Decodifica instrucoes tipo register"""
	instrucao_binaria = ""
	# Opcode
	instrucao_binaria += toStrBinary(instrucao[0],6)

	# 1 OP
	instrucao_binaria += toStrBinary(instrucao[2],5)

	# 2 OP
	instrucao_binaria += toStrBinary(instrucao[3],5)

	# Fonte
	instrucao_binaria += toStrBinary(instrucao[1],5)

	# Shamt
	instrucao_binaria += "00000"

	# Funct
	instrucao_binaria += toStrBinary(instrucao[0],6,"funct")

	#'\n' maroto
	instrucao_binaria += '\n'

	if(VERBOSE):
		print("decRegister():"," ".join(instrucao),"\n",instrucao_binaria,len(instrucao_binaria) - 1,"\n")

	return instrucao_binaria



def genPseudo(instrucao):
	"""Gera uma, ou mais, instrução (ões) real(is) a partir de uma pseudo instrucao"""
	instrucoes_reais = ""

	if(instrucao[0] == "move"):
		instrucao_real = []
		instrucao_real.append("add")
		instrucao_real.append(instrucao[1])
		instrucao_real.append(instrucao[2])
		instrucao_real.append("$zero")
		instrucoes_reais += decRegister(instrucao_real)

	elif(instrucao[0] == "not"):
		instrucao_real = []
		instrucao_real.append("nor")
		instrucao_real.append(instrucao[1])
		instrucao_real.append(instrucao[2])
		instrucao_real.append("$zero")
		instrucoes_reais += decRegister(instrucao_real)


	return instrucoes_reais


def decode(instrucoes):
	""" Decodifica lista de instruções"""
	instrucoes_binaria = ""
	for instrucao in instrucoes:
		if(isImmediate(instrucao)):
			print("decode(): detectada instrução imediata!")

			instrucoes_binaria += decImmediate(instrucao)

		elif(isPseudo(instrucao)):
			print("decode(): detectada pseudoinstrução!")
			for instrucao_real in genPseudo(instrucao):
				instrucoes_binaria += instrucao_real
		else:
			print("decode(): detectada instrução registrador!")
			instrucoes_binaria += decRegister(instrucao)

	return instrucoes_binaria
