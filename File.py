from Config import *

def parse():
	"""Lê e parseia o arquivo asm"""

    # Verifica se o arquivo é invalido por estourar index
	def parseIsInvalidFile(index):
		if(index > MAX_FILE):
			print("File.parse(): arquivo inválido!")
			exit(-1)

	def parseFileOperando(index,fonte_linha):
		operando = ""
		for char in fonte_linha[index:]:
			if(char == "," or char == '\n'):
				break
			parseIsInvalidFile(index)

			operando += char
			index += 1

        # Considera vírgula
		index += 1
		return operando

	instrucoes = []
	with open(INPUT_FILE_PATH) as fonte_arquivo:

		for fonte_linha in fonte_arquivo:
			index = 0

	        # Pega opcode
			opcode = ""
			for char in fonte_linha:
				if(char == " "):
					break
				parseIsInvalidFile(index)
				opcode += char
				index += 1

	        # Considera espaço da instrução para os operandos
			index += 1


			if((opcode in cod_instrucao) or (opcode in cod_pseudo)):
				
				# Separa por vírgulas
				instrucao = fonte_linha.split(',')

				# Separa por espaços para o opcode e adiciona os outros campos depois dele
				instrucao = instrucao[0].split(' ') + instrucao[1:]

				# Detecta se temos uma instrucao somente no arquivo de entrada
				if(instrucao[len(instrucao)-1][-1] == '\n'):
					instrucao[len(instrucao)-1] = instrucao[len(instrucao)-1][:-1]
				else:
					instrucao[len(instrucao)-1] = instrucao[len(instrucao)-1]

				# Tira por ventura quaisquer espaços nos campos
				index = 0
				for campo in instrucao:
					instrucao[index] = campo.replace(" ","")
					index += 1
				instrucoes.append(instrucao)
			else:
				print("File.parse() ERRO FATAL: instrução não reconhecida:",opcode)
				exit(-1)

	print(instrucoes)
	return instrucoes

def write(instrucao_binaria):
	"""Escrevre nossa saida"""
	with open(OUTPUT_FILE_PATH,"w") as binario_arquivo:
		binario_arquivo.write(str(instrucao_binaria))
