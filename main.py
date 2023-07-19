#!/usr/bin/python3
import File
import Core
from Config import *

instrucoes_binaria = (Core.decode(File.parse()))
if(VERBOSE):
	print(instrucoes_binaria)
File.write(instrucoes_binaria)
