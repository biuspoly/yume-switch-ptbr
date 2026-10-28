# Yume: tradução PT-BR e guia para jogar no Nintendo Switch

Tradução não oficial para **português do Brasil** do jogo de PC **Yume**, com as correções e o passo a passo
para jogá-lo no Nintendo Switch com custom firmware, usando o [Carafe](https://github.com/carafe-nx/carafe)
(Wine + DXVK no Switch).

> **Este repositório não contém o jogo.** Não há aqui executáveis, pacotes de dados, músicas nem imagens
> do Yume. Você precisa da sua própria cópia do jogo para PC. Os scripts só alteram arquivos que você já tem.

## O que tem aqui

| Arquivo | Para que serve |
|---|---|
| `make_ptbr.py` | Gera o `translations.txt` em português a partir do arquivo de traduções original do seu jogo. |
| `patch_frog.py` / `patch_frog.ps1` | Corrige o clique (e o toque na tela) na seleção de fases do mapa quando o jogo roda no Switch. |
| `Yume_d3dx9_native.reg` | Registro para o Carafe: obriga o Wine a usar a `d3dx9_24.dll` da Microsoft. Sem ele o jogo trava no início. |

## 1. Preparar o jogo no PC

Faça backup da pasta do jogo antes de começar.

### 1.1 Tradução para PT-BR
Requer [Python 3](https://www.python.org/downloads/).
```bat
cd "C:\caminho\do\Yume"
copy Data\translations.txt Data\translations_original.txt
python make_ptbr.py Data\translations_original.txt Data\translations.txt
copy Data\translations.txt Data\Music\translations.txt
copy Data\translations.txt Data\Voices\translations.txt
```
O script confere se o arquivo original tem as 153 entradas esperadas. Se não tiver, ele para sem gravar nada.

### 1.2 DirectX (d3dx9_24.dll)
O jogo precisa da `d3dx9_24.dll`. Baixe o
[DirectX End-User Runtimes (June 2010)](https://www.microsoft.com/en-us/download/details.aspx?id=8109)
da Microsoft, extraia o `Feb2005_d3dx9_24_x86.cab` (com o 7-Zip, por exemplo) e coloque a `d3dx9_24.dll`
ao lado do `Frog.exe`.

### 1.3 Resolução e tela cheia
Em `Data\options.dat`, ajuste para a tela do Switch:
```
Window=0
ScreenWidth=1280
ScreenHeight=720
```

### 1.4 Correção do clique no mapa (para o Switch)
Na seleção de fases, o jogo só aceita o clique se a janela sob o cursor for a dele. No Switch o Autorun
desenha o cursor por cima, então a fase fica selecionada mas não entra. O patch remove essa conferência
(6 bytes) e guarda o original como `Frog.exe.original`. No PC não muda nada.
```bat
python patch_frog.py "C:\caminho\do\Yume\Frog.exe"
```
Sem Python: clique com o botão direito em `patch_frog.ps1` e escolha **Executar com o PowerShell**,
ou rode `powershell -ExecutionPolicy Bypass -File patch_frog.ps1 "C:\caminho\do\Yume\Frog.exe"`.
O patch só é aplicado se o seu `Frog.exe` for exatamente a versão conhecida (o script confere o MD5).

> Status: a causa foi encontrada no código do jogo, mas o patch ainda está **em teste** no Switch.

## 2. Criar o NSP no Carafe

1. Instale o [Carafe](https://github.com/carafe-nx/carafe/releases) no PC e adicione a pasta do Yume
   (executável: `Frog.exe`).
2. **Configurações → Sistema → Registro → Importar .reg**: escolha `Yume_d3dx9_native.reg`.
3. **Configurações → Controles**: modo **Teclado e mouse**. Sugestão de botões:

   | Switch | Tecla |
   |---|---|
   | Direcional / analógico esquerdo | Setas |
   | B | Z (pulo) |
   | A | Mouse esquerdo |
   | Y | Espaço (ataque) |
   | X | C (olhar) |
   | L / R | X (defesa) |
   | + | Esc |

   O analógico direito e a tela de toque movem o cursor.
4. Se algum gráfico aparecer incompleto, abra **Gráficos → Opções do DXVK** (fica recolhido) → **Correções**
   e teste uma opção de cada vez: *Correção do tipo de textura (DX9)*, *Acesso direto a buffers (DX9)*,
   *Precisão dos cálculos de shader (DX9)*.
5. Gere o NSP e instale no Switch pelo **DBI** (MTP via USB).

Dica: o Carafe guarda a biblioteca na pasta Documentos. Se ela for sincronizada pelo OneDrive, mude a
"Pasta da biblioteca" nas configurações do Carafe para não enviar gigabytes para a nuvem.

## Agradecimentos

- **OnGames**, desenvolvedores do Yume. Se você gosta do jogo, apoie os criadores.
- **[Carafe](https://github.com/carafe-nx/carafe)** e **[Autorun](https://github.com/autorunhq/autorun)**,
  que levam jogos de Windows para o Switch.
- **[Wine](https://www.winehq.org)**, **[DXVK](https://github.com/doitsujin/dxvk)**, **[Mesa](https://mesa3d.org)**,
  FEX/Box64 e a comunidade **[Switchbrew](https://switchbrew.org)** / **[Atmosphère](https://github.com/Atmosphere-NX/Atmosphere)**.
- **DBI**, para instalar os NSPs.

Tradução e correções: **[biuspoly](https://github.com/biuspoly)**, com ajuda do Claude (Anthropic).

## Aviso

Projeto de fãs, sem fins lucrativos e sem ligação com os desenvolvedores do Yume ou com a Nintendo.
Yume e todo o seu conteúdo pertencem aos respectivos donos. Os scripts deste repositório estão sob a
licença MIT (veja `LICENSE`).
