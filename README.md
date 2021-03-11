# NFe-Analyzer-WEB

Olá, meu nome é Matheus. Certo dia eu estava trabalhando e chegou o início de um novo mês, nesse dia um dos funcionários da empresa que fornece o sistema de caixa para o mercado chegou, e instalou uma atualização e também me ensinou como eu deveria recolher os impostos e como verificar se está tudo certo. Compreendo que o correto seria o pessoal do financeiro da empresa do sistema cuidar disso, porém eu resolvi do mesmo jeito e isso garante uma certa agilidade, já que não tenho que esperar por eles.

Certo dia estava cursando a faculdade e dei um tempo para a aulas da faculdade e fui aprender python, tinha ganho um curso de biopython (Introdução à Programação para Bioinformática com Python) pela udemy então resolvi que já estava na hora de aprender uma linguagem poderosa, gostei muito do curso, mas até ver o poder e a facilidade do python não poderia ter automatizado minhas tarefas, a ideia só surgiu quando o professor mostrou como criar uma piperine gigantesca para automação de tarefas científicas, ai pensei porque não usar meu conhecimento para facilitar minha vida, assim surgiu o NFe Analyzer que mais tarde ganharia uma versão web.

Provavelmente você está se perguntando ok, ele fez um programa que automatiza as coisas mas o que exatamente? Bem permita-me explicar com base no programa de caixa usado no mercado, toda vez que uma venda é feita tem todo um processo por trás que gera, verifica e envia o cupom fiscal para a receita federal, em meio a tudo isso uma cópia interna é gerada em uma pasta que contém o mês seguido do ano exemplo: 012021, lá dentro contém todas as cópias em formato xml, os cupons que foram aprovados são novamente copiados para uma subpasta cujo nome e aprovada. No início de um novo mês preciso abrir um outro programa que cuida especificamente do gerenciamento de caixa preciso ir na parte de livro fiscal de saída, informar a data de início e fim do mês anterior, o programa gera um relatório em pdf com todos os valores que estão nos xmls com o id do cupom fiscal, o valor da compra, o total de itens, os impostos(roubo) e no final todo um cálculo e informe dos lucros da empresa tudo para facilitar a vida do governo na hora que decidir iniciar uma vistoria.

Bem, após entender o básico vamos a parte fiscal, como todos sabemos nenhum sistema é perfeito (principalmente esse) então existem algumas falhas que podem ocorrer xmls que podem não estar na pasta correta, xml que faltaram pois pode ter ocorrido algum problema com seu confirmamento no servidor da receita(ocorre bastante), falta de internet, então o programa mantém isso tudo guardado em um local diferente esperando que o usuário manualmente faça o reenvio isso pode gerar algum problema ou não. Como saber se tem alguma coisa errada? Simples abra o pdf em um lado da tela do outro a pasta aprovada e verifique manualmente o Id NFC-e e o nome do xml se ambos forem iguais esta tudo certo, agora imagina fazer isso em meio a mais 300 arquivos, e muito exaustivo, imagina em mercados enormes o trabalho que é fazer isso multiplicado por mais de mil clientes que o setor fiscal tem que atender, lembrando que é obrigatório que esteja exatamente tudo isso bem organizado e separado pois algum dia um agente da receita federal sempre pode bater a sua porta e pode te multar só por não feito a separação correta, mesmo eles tendo acesso a tudo e sabendo exatamente quanto cobrar(roubar) ele espera que você entregue tudo de forma correta podendo alegar que fez algo errado como esqueceu um xml acaba de ganhar multa uma por isso. 

Ok, agora que entendeu como funciona, e o nível da importância desse programa devemos falar sobre seu desenvolvimento e todos os processos pelo qual ele passou juntamente com  o desenvolvimento da minha lógica de programação.

O primeiro passo foi dado em outra versão desse programa fiz com que funcionasse e compilei assim poderia usar como um executável, ele funcionava na hora de fazer seu papel, porém sempre tem esse tipo de embate funcionar e ser funcional são coisas diferentes, todas as informações eram exibidas em um terminal não chegava a ser super confuso porém ficava muito técnico e estranho além de ser chato ver as informações lá (na real acho super legal, mas para quem não é da área de programação e uma coisa terrível de se entender) levando isso em conta resolvi que estava na hora de projetar algo novo porém eu não sabia como. Graças ao algoritmo do google alguns vídeos de python apareceram mostrando o uso de interface gráfica porém nessa hora eu estava em uma maratona python criada pelo Bruno Fraga do técnicas de invasão, lá eu tive uma série de novas aulas sobre python e pude aprendeu algo novo que mudou bastante minha mente Flask, isso mudou tudo esse micro framework seria a minha salvação, pois com a versão anterior do sistema aprendi algumas coisas que não podia repetir, a primeira interface gráfica ajuda bastante, segunda o windows 10 e um saco para abrir executáveis não assinados, além de ficar achando que e vírus sem nem ter visto se ele fez algum mal, a terceira coisa e que ficar salvando todo o log gerado em arquivos.txt e bem confuso.

Partindo da ideia que eu já sabia como o programa deveria funcionar ou seja já tinha boa parte do back end, decidir que nessa versão web deveria implementar uma nova funcionalidade após toda a análise o programa deveria compilar em um arquivo.rar contendo o nome do cliente seguido da data do mês e do ano o qual os impostos pertencem exemplo: Cliente 01.2021.

A partir daqui devo explicar como o programa funciona, inicialmente ocorre uma verificação para saber se algumas bibliotecas que por padrão não estão instaladas juntamente com o python possam ser instaladas tais como o Flask e duas que cuidam do pdf. agora uma página web é aberta informando algumas instruções como por a  pasta aprovada e do pdf na área de trabalho, pois é para isso que ela serve um uso rápido e objetivo. estando tudo certo e usada a biblioteca PyPDF4, porém quando eu estava criando uns arquivos para por como exemplo no git para que esse programa possa ser testado descobri um grande problema o PyPDF4 foi abandonado pelo criador e só oferece suporte a versões antigas do pdf, então encontrei uma biblioteca que é constantemente atualizada e que aceita todas as versões do pdf porém com uma perda na velocidade, então para contornar isso é feito um teste caso na primeira página do pdf o PyPDF4 não encontre nada uso a biblioteca pdfminer.six para abrir o pdf, agora obtenho todos os Id NFC-e presentes em todo o pdf. Na sequência obtenho o nome de todos os arquivos xml que estão na pasta aprovada. Salvo cada um em uma lista para facilitar o cruzamento de dados mais tarde.

Agora que tenho todos os dados que necessito tenho que fazer uma comparação, pois como já foi dito pode faltar algum elemento que pode conter alguma inconsistência, por algum motivo usando a versão antiga do meu programa pude notar que um Id NFC-e estava clonado, então o programa já cria uma tratativa para isso. 
 
Iniciando o cruzamento de dados, na versão anterior tinha feito todo um algoritmo bem mais complexo à toa, pois teria sido muito mais fácil utilizar as ferramentas que o próprio python nos fornece por isso nessa versão utilizo listas. Como é feito o cruzamento de dados, inicialmente pegamos elemento por elemento da lista obtida no pdf e comparamos elemento por elemento que estão na lista obtidas na pasta aprovada, caso o elemento da lista pdf 
ache seu par e adicionado em um dicionário chamado resultados o elemento em questão e seu par,  caso não ache seu par e feito uma tratativa de erro é adicionado na lista citada anteriormente junto a uma mensagem de par não encontrado. A segunda parte do cruzamento de dados é feita da seguinte forma pegando elemento por elemento da lista de xmls verificamos se os Id NFC-e desta lista encontram seu par na lista pdf caso não são salvos em uma nova lista chamada deleta_xml pois esses devem ser excluídos.

Agora que o cruzamento de dados foi finalizado, o programa exibe uma tela com o resultado caso haja algum erro terá um aviso sobre esse erro, como corrigir, juntamente com o motivo de tal erro ter surgido, e um botão para verificar o log da do cruzamento de dados contendo o Id NFC-e encontrado no pdf juntamente com o arquivo xml correspondente. Caso algum xml esteja indevidamente na pasta aparece uma mensagem pedindo para clicar em deletar, para que o programa delete o xml indevido e faça uma nova busca a fim de ter certeza do resultado. Caso encontre alguma duplicação, infelizmente o pdf já foi gerado, assim isso é um bug do sistema de caixa, então o máximo que pude fazer é informar que existe.

Caso esteja tudo correto aparece uma tela onde o usuário põe o nome do cliente e clica em compilar, assim o programa obtém o nome do cliente põem a primeira inicial maiúscula e juntamente obtém o mês atual e subtrai um pos estamos lidando com o mês anterior o ano deve ser mantido o mesmo, claramente criei uma tratativa caso seja o primeiro mês significa que estamos lidando com os dados do ano anterior então neste caso é subtraído um ano para que possa obter o resultado correto. Exemplo: Cliente 01.2021 .

Recentemente tive uma entrevista de emprego na AVEC, infelizmente não consegui a vaga pois eles queriam um cientista de dados, mas a questão mais importante foi saber que o cientista que me entrevistou gostou do projeto e pediu para que algumas atualizações fossem feitas e o projeto tivesse uma implementação futura na AWS, no momento que você está lendo isso ainda estou estudando para que isso possa ser possível, apesar de ter explicado que esse projeto tinha a finalidade de funcionar localmente pois, minha ideia era que mesmo sem internet qualquer pessoa responsável pelo financeiro poderia concluir seu trabalho, já que foi tudo projetado para ser offline.

Se você chegou até aqui lendo tudo agradeço pela atenção, caso não volta e lê tudo, pois se eu dou atenção a detalhes como este, espero o mesmo de alguém que se interessou por esse projeto.   
 

 
