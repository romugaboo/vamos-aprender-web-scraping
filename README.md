# 💻 Vamos Aprender Web Scraping!

Este repositório tem como objetivo ensinar o básico de **web scraping**, focando no uso da biblioteca **Selenium** com Python para coletar dados de sites com conteúdo dinâmico.

## 📚 O que é Web Scraping?

**Web scraping** (ou raspagem de dados) é o processo de extrair informações automaticamente de sites. Ele permite coletar grandes volumes de dados de forma estruturada e reutilizável.

## 🔧 Ferramentas de Web Scraping

As principais abordagens são:

- 🔗 [**JSON direto da API**](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview): ideal quando a página consome dados de uma API. Basta interceptar e coletar o link.
- 🔗 [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): ideal quando os dados estão no HTML estático e não há necessidade de interação (cliques, rolagens).
- 🔗 [**Selenium**](https://www.selenium.dev/documentation/webdriver/): necessária quando o conteúdo é carregado dinamicamente via JavaScript (AJAX) ou há interações na página.

**Regra prática:**

- Se não precisar clicar: **use BeautifulSoup** (mais rápido e estável).
- Se precisar interagir com a página: **use Selenium**.

## 🚀 Por que aprender Selenium?

Apesar de mais pesado e lento, **Selenium** é o mais versátil. Ele permite:

- Simular cliques, rolagens e interações humanas
- Coletar dados dinâmicos (ex: AJAX)
- Testes automatizados end-to-end (E2E), inclusive em ambientes de produção (como AWS)

Saber usar o Selenium cobre praticamente todos os cenários. A transição para BeautifulSoup depois é simples.

## 🧪 Uso intenso do DevTools

Durante o desenvolvimento, usamos frequentemente o **DevTools (F12)** do navegador, especialmente a aba **Elements** para inspecionar a estrutura do HTML. Isso ajuda a:

- Encontrar o seletor correto dos elementos (como `div.product`, `span.price`, etc)
- Copiar XPaths ou seletores CSS rapidamente

Saber navegar bem no DevTools é essencial para scraping eficiente.

## 🌍 Navegador usado

Apesar da preferência pessoal pelo **Firefox**, o projeto foi feito usando **Google Chrome** porque:

- O Selenium tem integração mais estável com o **ChromeDriver**
- O Firefox com GeckoDriver impõe limites de uso e pode apresentar travamentos ou incompatibilidades com alguns sites modernos
- A maioria dos exemplos e documentação da comunidade está voltada para o Chrome

Você pode adaptar o código para Firefox se quiser, mas o Chrome é mais confiável para scraping automatizado.

## 🌐 Site para prática

Vamos praticar com o seguinte site:

- 🔸 **AJAX (com cliques necessários)**  
  https://webscraper.io/test-sites/e-commerce/ajax  
  Requer Selenium pois o conteúdo dos produtos só aparece após o clique.

- 🔹 **Site estático (sem necessidade de clique)**  
  https://webscraper.io/test-sites/e-commerce/static  
  Ideal para BeautifulSoup, pois o HTML é carregado diretamente.

## 🧠 Estratégia da Aula

- Vamos **extrair dados** de todas as categorias e subcategorias do site com AJAX.
- Os dados extraídos serão:

  - Categoria
  - Subcategoria
  - Nome do produto
  - Preço
  - Descrição
  - Número de reviews
  - Avaliação (estrelas)

- Todos os dados serão salvos em um arquivo `.csv`.

Durante a execução, exibiremos o progresso no terminal para verificar se o AJAX carregou tudo corretamente.

**Importante:**  
Vamos focar apenas na **extração dos dados**. A **limpeza e análise** serão feitas separadamente.

## 💾 Por que salvar só os dados?

Separar scraping da análise é **boa prática**:

- Garante que você salve os dados mesmo se o site sair do ar ou a internet cair
- A coleta fica mais rápida e focada
- Você pode trabalhar offline com os dados depois

## ⚙️ Requisitos para rodar o projeto

- Python 3.x ou superior
- Google Chrome instalado

Instale as dependências com:

```bash
pip install selenium
```

## 🧩 Extensões do VSCode úteis

- **[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)**
  Suporte completo à linguagem Python no VSCode. Permite debug, linting, autocomplete, execução e integração com ambientes virtuais.

- **[Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)**
  Executa scripts Python com um clique ou atalho (`Ctrl+Alt+N`). Ideal para testar rapidamente funções ou scripts completos sem configurar o terminal.

- **[Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)**
  Destaca automaticamente colunas de arquivos `.csv` com cores diferentes, facilitando a leitura e debug de dados tabulares diretamente no VSCode.

- **[Markdown Viewer Enhanced](https://marketplace.visualstudio.com/items?itemName=MarkdownViewer.enhanced-md-editor)**
  Visualiza arquivos `.md` com renderização real, facilitando a edição de READMEs e documentação diretamente dentro do editor.

- **[Windsurf](https://marketplace.visualstudio.com/items?itemName=Codeium.codeium)**
  Ferramenta de autocompletar com IA. Sugere trechos de código inteiros em tempo real, com base no contexto do que você está escrevendo.

## 📁 Análise Posterior

Após a coleta, você pode tratar, analisar e visualizar os dados com:

- 📊 [**Pandas**](https://pandas.pydata.org/docs/): carregar o CSV em um DataFrame, filtrar, agrupar e calcular métricas.
- 📈 [**Matplotlib**](https://matplotlib.org/stable/index.html) / [**Seaborn**](https://seaborn.pydata.org/): gerar gráficos visuais.
- 📋 **Excel**: nem sempre a formatação fica correta ao abrir o CSV diretamente no excel. Se quiser algo mais visual, abra uma planilha em branco, vá para a aba dados, clique em "De Text \ CSV", escolha o arquivo a ser convertido e salve como `.xlsx`.

## 🧩 Desafio (Extra)

- ✅ Utilize um bloco `try/except` para garantir que os dados coletados até o momento sejam salvos mesmo se algo der errado (ex: internet caiu, exceção inesperada, luz acabou).
- ✅ Pegue as mesmas informações utilizando uma técnica que não foi ensinada no vídeo (leia a documentação oficial do selenium).
- ✅ Clique em cada produto individualmente e extraia a capacidade do HD e a cor (caso existam essas informações na página do produto).
 
 