# recortar_etiqueta_postagem
Recorte suas etiquetas da Shopee, Mercado Livre e Olx.
Para impressão em uma única página.
Resolvi desenvolver esse código, digo de antemão que não sou especialista em Python.
Consegui com esforço pessoal e ajuda de algumas pessoas.
Fique a vontade para modificar e ajustar para o seu uso.
Eu criei 3 arquivos .py, um para cada plataforma. 
E além disso, a única forma que consegui implementar usa um arquivo .pdf temporário de recorte.

-----------------------------------
Atualização em 10-10-2024
Adicionado Arquivos na Pasta GUI.
Cada arquivo faz o recorte do arquivo pdf da respectiva empresa(ML, Shopee, OLX)
Eles possuem interface gráfica para facilitar o uso.
Consegui modificar o código com a ajuda do ChatGpt.
Boa sorte! E boas vendas a todos e todas!

--------------------------------------------------------------
Atualização em 11/01/2025
Atualizado área de corte etiqueta Shopee para emissores de NFe.
Caso a sua venda tenha apenas declaração de conteúdo, mantenha a área de corte conforme parâmetros a seguir:
pagina 1 (0, 0, 310, 410)
pagina 2 (2, 0, 580, 551)

Caso faça emissão de NFe, será preciso mesclar os 2 PDFs, depois excluir a página com a declaração de conteúdo (Isso pode ser feito gratuitamente no site ilovepdf em duas etapas.
A área de corte nesse caso está assim:
pagina 1 (0, 0, 310, 410)
pagina 2 (0, 90, 580, 792)

Adicionado o arquivo 'GUI_Recorte_Etiqueta_All.py'. Esse arquivo único recorta etiquetas das 3 plataformas. 

SUCESSO!!!
----------------------------------------------------------------------------------------------------------------




