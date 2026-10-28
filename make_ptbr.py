import textwrap, sys

SRC = sys.argv[1]
DST = sys.argv[2]

def wrap(*paras, width=70):
    """Junta parágrafos com quebras \\n (literal), como o jogo espera.
    Um parágrafo vazio vira linha em branco; um parágrafo começando com '* '
    é fala de personagem e ganha o recuo '   * ' usado no original."""
    out = []
    for p in paras:
        if p == "":
            out.append("")
            continue
        prefix = ""
        if p.startswith("* "):
            prefix, p = "   - ", p[2:]
        lines = textwrap.wrap(p, width=width - len(prefix))
        lines[0] = prefix + lines[0]
        out.extend(lines)
    return "\\n".join(out)

PT = {
 0: "",
 1: "      %d / %d sonhos",
 2: "      Carta encontrada",
 3: wrap("* Kisaki, a princesa dos sonhos, perdeu seu fragmento da pedra. "
         "Ela está perdida, derrotada no último ataque das sombras. Mas ainda "
         "não é tarde para ela: você ainda pode viajar até a região dela para "
         "obter o segundo fragmento. Se você destruí-lo, como a princesa "
         "desejava, ela voltará e reinará sobre um Mundo dos Sonhos sem "
         "conflitos nem dor. Mas se o seu fragmento for destruído, os "
         "pesadelos tomarão conta. Parta agora, mas quando o poder estiver em "
         "suas mãos, lembre-se: não há alegria sem tristeza, nem coragem sem medo."),
 4: "Modelagem 3D e Animação",
 5: wrap("Uma figura feminina se aproxima de Yin, cercada de formas ameaçadoras "
         "que ela parece liderar com orgulho. Seu rosto mostra uma mistura de "
         "surpresa e angústia, como quem reencontra uma velha lembrança que "
         "julgava perdida só para perdê-la de novo.",
         "* Meu fragmento! Quem é você, garoto, invadindo o meu reino para "
         "roubar o que não lhe pertence? Devolva a minha pedra, rápido! Os "
         "pesadelos estão se multiplicando, minha resistência enfraquece a "
         "cada dia, não posso defender o meu reino sem ela! Me dê!"),
 6: wrap("Diz a lenda que cada sonho é um ser diferente, que nasce, sente e "
         "vive sem nós, num mundo além das nuvens. Os sonhos são a nossa "
         "inspiração, a nossa alegria e os nossos medos, cada um o ponto de "
         "partida de um novo dia. Por milhares de anos eles viveram em "
         "harmonia, nos amparando sem nunca revelar sua verdadeira natureza.",
         "",
         "O que aconteceria se essa harmonia fosse perturbada?"),
 7: "Aplicar novas configurações",
 8: "Arte Conceitual Adicional",
 9: "Efeitos Avançados",
 10: "Ainda assim, alguns lugares ficam longe demais. Tente pular na parede e você alcançará as plataformas mais altas.",
 11: "Todos os Checkpoints Ativados",
 12: "Mapa Todo Visível",
 13: wrap("Entre as nuvens, invisível para quem não se importa em vê-lo, existe "
          "um castelo onde nenhum sonho habita. Yin está lá agora, em busca de "
          "respostas. Na sala do trono encontramos um ser mais antigo que o "
          "próprio tempo, cuja voz soa como uma chuva distante.",
          "* A harmonia foi quebrada, e o mundo dos sonhos caiu. Durante "
          "milhares de anos, todas as esperanças e todos os medos presentes no "
          "coração das coisas foram um só, mas a pedra finalmente se partiu e "
          "agora pesadelos e sonhos lutam pelos seus fragmentos."),
 14: "Animação",
 15: "Anna Gómez",
 16: "Antonio Sánchez",
 17: "Arte",
 18: "Ataque",
 19: "Voltar",
 20: wrap("Mas outra vontade, sombria e antiga, se move neste lugar. Das "
          "sombras da floresta surgiram todo tipo de seres extraordinários. "
          "Eles saltam sobre a pedra como se guiados por uma mão invisível. Na "
          "confusão, as sombras se chocam e se embaralham umas com as outras: "
          "é uma batalha, e Yin não pode fazer muito além de se salvar. Num "
          "certo momento, a pedra escapa de sua mão e se perde entre as "
          "rachaduras do chão. A última coisa de que ele se lembra é de saltar "
          "para alcançá-la e de uma escuridão fria o envolvendo."),
 21: "Galeria de Cartas",
 22: "Cartas encontradas",
 23: "Escolher outro jogo",
 24: "Continuar",
 25: "Continuar jogo atual",
 26: "Personalizar Controles",
 27: "O perigo espreita em cada canto do Mundo dos Sonhos. Cuidado! Qualquer encontro com ele pode ser fatal.",
 28: "David Font \\\"synchrnzr\\\"",
 29: "Defesa",
 30: "Desativado",
 31: "Baixo",
 32: "Sonhos capturados",
 33: "Sonhos/Carta Restaurados",
 34: "Ativado",
 35: "Produtores Executivos",
 36: "Sair",
 37: wrap("Por fim, Yin tomou uma decisão, a única que lhe permitiria voltar ao "
          "seu velho mundo como ele o conhecia. E foi assim que o Mundo dos "
          "Sonhos voltou a ser um só, como sempre havia sido."),
 38: "Tela Cheia",
 39: "Jogo %d (%d%% concluído)",
 40: "Jogo Salvo",
 41: "Jogo concluído",
 42: "Já tentou apertar os botões de cima e de ataque ao mesmo tempo? Um ataque alto pode ser útil contra monstros voadores.",
 43: "Fundos em alta qualidade",
 44: "Vou te contar um segredo: cada fase esconde uma bela carta decorada. Ninguém jamais conseguiu reunir todas.",
 45: "Vidas Infinitas Desligadas",
 46: "Vidas Infinitas Ligadas",
 47: "Tem algum lugar que você não alcança? Tente apertar o botão de pulo duas vezes.",
 48: "Parece que alguns sonhos ganharam vida e se transformaram em criaturas perigosas. Use o botão de ataque (barra de espaço) para atacá*las com a espada e o botão secundário (Ctrl direito) para se proteger.",
 49: "Joan Guardiet",
 50: "José Luis Cebrián",
 51: "Pulo",
 52: "Esquerda",
 53: "Fase Concluída",
 54: "Segredo da Fase 1",
 55: "Fase 1*1", 56: "Fase 1*2", 57: "Fase 1*3", 58: "Fase 1*4", 59: "Fase 1*5",
 60: "Chefe da Fase 2",
 61: "Segredo da Fase 2",
 62: "Fase 2*1", 63: "Fase 2*2", 64: "Fase 2*3", 65: "Fase 2*4", 66: "Fase 2*5", 67: "Fase 2*6",
 68: "Chefe da Fase 3",
 69: "Segredo da Fase 3",
 70: "Fase 3*1", 71: "Fase 3*2", 72: "Fase 3*3", 73: "Fase 3*4", 74: "Fase 3*5", 75: "Fase 3*6",
 76: "Chefe da Fase 4",
 77: "Segredo da Fase 4",
 78: "Fase 4*1", 79: "Fase 4*2", 80: "Fase 4*3", 81: "Fase 4*4", 82: "Fase 4*5", 83: "Fase 4*6",
 84: "Carregando",
 85: "Olhar",
 86: "Os portais mágicos ajudam a recuperar a vida que você perdeu. Você também pode voltar a portais pelos quais já passou. Aperte para baixo para ser teletransportado até lá.",
 87: "Marc Calvelo",
 88: "Modelagem e",
 89: "Modelagem e Animação",
 90: "Música e",
 91: "Música e Design de Som",
 92: "Não",
 93: "Normal Map",
 94: "Ideia Original",
 95: "Aperte a tecla %s",
 96: "Pausado",
 97: "Pau Ors",
 98: "Programadores",
 99: "Gerente de Projeto",
 100: "Raúl Morales",
 101: "Remover cortes na imagem (V*Sync)",
 102: "Restaurar Padrões",
 103: "Voltar ao Menu Principal",
 104: "Voltar ao Mapa",
 105: "Direita",
 106: "Salvar e Sair",
 107: "Resolução da Tela",
 108: "Escolha o seu jogo",
 109: "Configurações",
 110: "Desde que a harmonia foi quebrada, o Mundo dos Sonhos mergulhou no caos total. Veja com seus próprios olhos: use as setas para andar e pular.",
 111: "Suavizar bordas",
 112: "Design de Som",
 113: "Começar um novo jogo",
 114: "Desenhos originais (terceiro mundo)",
 115: "Desenhos originais (primeiro mundo)",
 116: "Yin e o Deus Sombrio",
 117: "Yin",
 118: "Monstro voador do primeiro mundo",
 119: "Monstro do primeiro mundo",
 120: "Desenhos originais (monstro*bola descartado da versão final do jogo)",
 121: "Deus Branco dos sonhos",
 122: "Esboço original do Deus Sombrio",
 123: "Desenhos originais",
 124: "Desenhos originais (segundo mundo)",
 125: "Desenhos originais (segundo mundo)",
 126: "Desenhos originais (segundo mundo)",
 127: "Desenhos originais (terceiro mundo)",
 128: "Yin (poses e modelo definitivo)",
 129: "Desenhos originais (monstro*soldado do quarto mundo)",
 130: "Monstro*inseto do primeiro mundo",
 131: "Esboço do chefe final do primeiro mundo (descartado do jogo)",
 132: "Desenhos originais (monstro do primeiro mundo)",
 133: "Deus Sombrio",
 134: "Yin",
 135: "Esboços de Yin em movimento",
 136: "Esboços de Yin em movimento",
 137: "Esboço original de Yin",
 138: "Esboços de Yin em movimento",
 139: "Esboços de Yin em movimento",
 140: "Esboços de Yin em movimento",
 141: "Esboços de Yin em movimento",
 142: "As gemas que você vê à sua frente são sonhos preciosos que não deveriam estar flutuando soltos. Pegue*as e leve*as até um portal como este. Se reunir todas, elas podem revelar um segredo.",
 143: "Os espectros do castelo do Deus das Trevas são imortais. Fuja deles.",
 144: "Estas águas não parecem seguras. Cuidado para não cair nelas.",
 145: "Essas plataformas de gelo não parecem seguras. Cuidado para não escorregar.",
 146: "Essas águas não parecem seguras. Cuidado para não cair nelas.",
 147: "Cima",
 148: "Mundos de Yume",
 149: "Sim",
 150: wrap("Yin teve dificuldade para acordar, como se não quisesse voltar. Mal "
          "consegue abrir os olhos, mas quando finalmente consegue, a visão é "
          "desconcertante, cheia de cores estranhas que ele nunca viu antes. Ele "
          "próprio mudou: a água reflete outra pessoa, vestida com roupas "
          "exóticas, de aparência ameaçadora, com uma espada numa mão e na "
          "outra uma pedra estranha que não para de brilhar, como se o "
          "alertasse de algum perigo."),
 151: wrap("Yin tinha os dois fragmentos da pedra e o destino do mundo em suas "
           "mãos. Uma voz parecia vir da pedra escura: \\\"somos o medo e o "
           "perigo, somos cada obstáculo que você terá de superar. Damos sentido "
           "à sua vida, porque sem nós não há objetivo, nem coragem, nem vitória "
           "possível\\\". Outra voz parecia sair da pedra branca: \\\"somos a "
           "alegria e o prazer, somos cada momento que você vai querer lembrar. "
           "Damos sentido à sua vida, porque sem nós não há esperança, nem "
           "recompensa ao fim da jornada\\\"."),
 152: wrap("Yin tem a pedra de novo, mas isso não resolveu muita coisa. Ele se "
           "sente preso neste mundo frio e distante. Mas logo descobre que não "
           "está sozinho: um ser, antigo como o vento nas rochas, habita as "
           "profundezas deste mundo. O velho dragão agora está livre. Ele se "
           "surpreende com a presença do garoto ali, trazendo a pedra consigo.",
           "* Você carrega um fardo que não compreende, garoto. Sei que anseia "
           "voltar, mas não sabe como. Venha, suba nas minhas costas e vamos "
           "voar pelos céus. Você encontrará respostas para as suas perguntas."),
}

raw = open(SRC, 'rb').read().decode('latin-1')
keys = [l[1:] for l in raw.split('\r\n') if l.startswith('*')]
assert len(keys) == len(PT) == 153
# Formato que o Frog.exe realmente lê (ver o leitor em 0x40dd50 e o gravador em 0x40ded0):
#   -<texto original>\n*<tradução>\n\n   (chave primeiro, só LF)
# No arquivo da versão italiana a ordem estava invertida e os hífens viraram '*',
# por isso ele nunca era aplicado.
out = []
for i, k in enumerate(keys):
    if not k:
        continue
    if not k.startswith('Texto Carta'):
        k = k.replace('*', '-')
    out.append('-' + k + '\n*' + PT[i].replace('*', '-') + '\n\n')
data = ''.join(out).encode('latin-1')
open(DST, 'wb').write(data)
print("ok", len(out), "entradas,", len(data), "bytes")
