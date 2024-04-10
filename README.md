# Web Scraping

Web Scraping das últimas notícias do site spacemoney.com usando Python, usandos as seguintes biliotecas:
  * Selenium.
  * OS e time.

Foi usado **driver.currently_url** para trocar link de propagandas do google ads por link de pesquisa de noticias pois o site estava abrindo muitos ads. Também foi usado o **try exception** para tratar exceções.

**Relatório sobre Automação de Coleta de Notícias do Site SpaceMoney**

**Objetivo:**
O objetivo deste relatório é fornecer uma visão geral do código desenvolvido para automatizar a coleta de notícias do site SpaceMoney, utilizando a biblioteca Selenium em Python.

**Resumo do Código:**
O código em questão utiliza a biblioteca Selenium para controlar um navegador web automatizado (no caso, o Microsoft Edge) e navegar até a página de últimas notícias do site SpaceMoney. Em seguida, ele seleciona a primeira notícia disponível, extrai o texto da notícia e salva em um arquivo de texto no sistema local.

**Detalhes do Código:**
1. **Inicialização do Navegador:** O código inicializa o navegador Microsoft Edge utilizando a biblioteca Selenium.

2. **Acesso à Página de Últimas Notícias:** Após a inicialização, o navegador é direcionado para a URL da página de últimas notícias do site SpaceMoney.

3. **Espera pela Carregamento da Página:** O código espera 1 segundo para garantir que a página seja completamente carregada.

4. **Maximização da Janela do Navegador:** A janela do navegador é maximizada para garantir uma visualização adequada da página.

5. **Gestão de Pop-up:** O código verifica se há um botão de pop-up com o ID 'adopt-reject-all-button' e o fecha, caso presente.

6. **Seleção da Primeira Notícia:** O código localiza o link para a primeira notícia na página e clica nele.

7. **Verificação e Atualização da URL:** Em seguida, é verificado se a URL contém '#google_vignette' e, se sim, essa parte é removida da URL para evitar problemas de carregamento.

8. **Coleta de Texto da Notícia:** O código localiza os parágrafos que contêm o texto da primeira notícia e os armazena em uma lista.

9. **Espera para Garantir Carregamento Completo:** É aguardado 2 segundos para garantir que todo o texto da notícia seja carregado adequadamente.

10. **Salvamento do Texto em Arquivo:** O texto da notícia é escrito em um arquivo de texto chamado 'artigo_noticia_1.txt' no sistema local.

11. **Espera para Garantir que o Arquivo seja Salvo:** É aguardado 1 segundo para garantir que o arquivo de texto seja salvo corretamente.

12. **Download do Arquivo:** Por fim, o código utiliza o módulo 'os' para iniciar o download do arquivo de texto gerado para o sistema local.

**Conclusão:**
O código desenvolvido é eficaz para automatizar o processo de coleta de notícias do site SpaceMoney. Ele demonstra o uso prático da biblioteca Selenium para interagir com elementos de uma página da web e extrair informações específicas. No entanto, é importante observar que a eficácia desse código pode depender da consistência da estrutura da página do site SpaceMoney e pode exigir ajustes se houverem alterações na estrutura do site.
