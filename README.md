# 🧾 Recorte de Etiquetas em PDF [etiquetas em papel A4] – Shopee, Mercado Livre e OLX
<img src="https://github.com/andersonsistemas/recortar_etiqueta_postagem/blob/main/Recorte_PDF_PY.png" alt="Recorte de Etiquetas em PDF">

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
 -Python (recomenda-se a versão mais recente) - http://python.org/downloads/
 -PyMuPDF

Instalação:
pip install PyMuPDF

🛠️ Como usar
Certifique-se de que o Python está instalado.
Instale o módulo PyMuPDF com o comando acima.
Execute o script GUI_Recorte_Etiqueta_All.py.
Selecione o PDF original da etiqueta (com duas páginas).
O sistema irá gerar um novo arquivo com o conteúdo ajustado para caber em uma única página.

📝 Observações importantes
Este script não é oficial e não possui vínculo com Shopee, Mercado Livre ou OLX.
O corte foi calibrado para PDFs que possuem declaração de conteúdo em uma segunda página com baixo aproveitamento.

No caso de etiqueta da Shopee:
Se você emite NFe (Nota Fiscal Eletrônica), será necessário:
Mesclar os dois PDFs (etiqueta + NFe)
Excluir a página de declaração de conteúdo (pode usar gratuitamente o iLovePDF em duas etapas - Juntar e Organizar PDF )

🧮 Áreas de corte utilizadas:
▶️ Caso sua venda tenha apenas declaração de conteúdo:
Página 1: (0, 0, 310, 410)
Página 2: (2, 0, 580, 551)

▶️ Caso tenha emissão de NFe:
Página 1: (0, 0, 310, 410)
Página 2: (0, 90, 580, 792)

🤝 Agradecimentos
Esse projeto foi desenvolvido com esforço pessoal, contando com a ajuda da comunidade Python Brasil e também com sugestões do ChatGPT da OpenAI.

Sinta-se à vontade para adaptar, melhorar ou reutilizar o código conforme suas necessidades!

✨ Contribuição
Sugestões, melhorias ou correções são sempre bem-vindas!
Abra um pull request ou issue aqui no repositório.

🙌 Boa sorte e boas vendas!
Sucesso a todos e todas!
