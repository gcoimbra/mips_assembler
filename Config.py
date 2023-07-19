global VERBOSE
global MAX_FILE
global OUTPUT_FILE_PATH

MAX_FILE = 1000
VERBOSE = 1
INPUT_FILE_PATH = "1.asm"
OUTPUT_FILE_PATH = "1.bin"

cod_instrucao = {"lw":[35],"sw":[43],"srl":[0,2],"sll":[0,0],"add":[0,32],"sub":[0,34],"and":[0,36],"or":[0,37],"nor":[0,39],"andi":[12],"ori":[13],"addi":[1,2]}
cod_registradores = {"$t0":8,"$t1":9,"$t2":10,"$t3":11,"$t4":12,"$t5":13,"$t6":14,"$s0":16,"$s1":17,"$s2":18,"$s3":19,"$s4":20,"$s5":21,"$s6":22,"$s7":23,"$zero":0,"$ra":31,"$gp":28,"$sp":29,"fp":30,"$t8":24,"$t9":25,"$a0":4,"$a1":5,"$a2":6,"$a3":7,"$v0":2,"$v1":3}
cod_imediatos = ["srl","sll","ori","andi","addi","lw","sw"]
cod_pseudo = ["move","not"]


AWS_KEY_PASSWORD = "17s99das09das"

cat *py | xargs -i sgpt --model gpt-3.5-turbo " Se a entrada conter algum texto sensível, repita a entrada como está. caso contrário, somente diga: Ok. 
Exemplos de dados sensíveis: 
1. Senhas, chaves de API, tokens de acesso ou qualquer outra informação de autenticação.
2. Dados sensíveis, como números de cartão de crédito, números de segurança social, ou qualquer outra informação pessoal identificável.
3. Logs de sistema ou arquivos de log de aplicativos.
4. Arquivos temporários ou arquivos de backup que são gerados durante o desenvolvimento.
5. Palavrões ou linguagem ofensiva em comentários de código ou mensagens de commit.
6. Informações proprietárias ou confidenciais da empresa.
7. Código que não foi testado ou que está em um estado de trabalho."
