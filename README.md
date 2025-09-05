# 🧾 Recorte de Etiquetas em PDF [etiquetas em papel A4] – Shopee, Mercado Livre e OLX (Atualizado 2.0)
<img src="https://github.com/andersonsistemas/recortar_etiqueta_postagem/blob/main/recorte2.0.png" alt="Recorte de Etiquetas em PDF 2.0">

Atualização 2.0 (Vendedores da Shopee tem duas opções) DC para etiquetas com Declaração de Conteúdo e NFe para etiquetas com Nota Fiscal eletrônica na segunda página.
Economize papel e otimize a impressão das suas etiquetas!
Este projeto em Python foi criado para reorganizar etiquetas em PDF, recortando o conteúdo de duas páginas e ajustando para impressão em uma única folha A4.
Ele é especialmente útil para vendedores que atuam em plataformas como Shopee, Mercado Livre e OLX, onde muitas vezes a primeira página da etiqueta ocupa apenas 40% do espaço.

✅ Funcionalidade
📦 Junta o conteúdo útil de duas páginas em uma única página A4.
✂️ Recorta áreas específicas de cada página com base em coordenadas predefinidas.
🖨️ Ideal para impressão em impressoras jato de tinta ou laser.
❌ Não compatível com impressoras térmicas (como Zebra TLP2844).
💾 Gera um arquivo temporário temp.pdf com o resultado final.


📦 Requisitos:
 
 Python (recomenda-se a versão mais recente) - http://python.org/downloads/
 
 PyMuPDF

Instalação:

pip install PyMuPDF

🛠️ Como usar
Certifique-se de que o Python está instalado.
Instale o módulo PyMuPDF com o comando acima.
Execute o script GUI_Recorte_Etiqueta_All.py.
Selecione o PDF original da etiqueta (com duas páginas).
O sistema irá gerar um novo arquivo com o conteúdo ajustado para caber em uma única página.

📝 Observações importantes:

Este script não é oficial e não possui vínculo com Shopee, Mercado Livre ou OLX.
O corte foi calibrado para PDFs que possuem declaração de conteúdo em uma segunda página com baixo aproveitamento.

# Se você usa Etiqueta A4 da Shopee:
Se você emite NFe (Nota Fiscal Eletrônica), selecione Shopee(NFe):
Antes, mesclar os dois PDFs (etiqueta + NFe) e excluir a página de declaração de conteúdo.
Se só vende com a declaração de conteúdo, selecione Shopee (DC).

✅Adicionado Ferramenta para organizar os arquivos PDF da Shopee, basta selecionar os dois arquivos e  ❌ excluir a página de declaração de conteúdo. Em seguida 💾 salvar o novo arquivo.
<img src="https://github.com/andersonsistemas/recortar_etiqueta_postagem/blob/main/organizador_Shopee.png" alt="Organizador de PDF Shopee">


🤝 Agradecimentos
Esse projeto foi desenvolvido com esforço pessoal, contando com a ajuda da comunidade Python Brasil e também com sugestões do ChatGPT da OpenAI.

Sinta-se à vontade para adaptar, melhorar ou reutilizar o código conforme suas necessidades!

Contribuição:

Sugestões, melhorias ou correções são sempre bem-vindas!
Toda ajuda é bem-vinda e me motiva a continuar trazendo conteúdo gratuito pra vocês.
Se quiser ajudar com o pix:

paidowifi@gmail.com

Fique a vontade para abrir um pull request ou issue aqui no repositório.

🙌 Boa sorte e boas vendas!
Sucesso a todos e todas!
