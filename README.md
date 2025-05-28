# Código em Python Para Recortar etiquetas de postagem em papel A4

Econimize papel e Recorte o PDF de suas etiquetas da Shopee, Mercado Livre e Olx.
Para impressão em uma única página A4.
Desenvolví esse código para me ajudar a economizar papel.
Com isso economizei cerca de 40% de papel.
Acho desnecessário imprimir a declaração de conteúdo ou NFe em uma única folha.
Confesso, que eu consegui com esforço pessoal e ajuda de algumas pessoas. E uma ajudinha do ChatGpt.
Fique a vontade para modificar e ajustar para o seu uso.
A única forma que consegui implementar usa um arquivo temp.pdf temporário de recorte.

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

Adicionado o arquivo 'GUI_Recorte_Etiqueta_All.py'.
Esse arquivo único recorta etiquetas das 3 plataformas. 

Boa sorte! E boas vendas a todos e todas! SUCESSO!!!
----------------------------------------------------------------------------------------------------------------




