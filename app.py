import turtle
from pathlib import Path

# ==========================================
# FOME BATEU, AQUI RESOLVEU!
# Livro de receitas com Turtle
# ==========================================

tela = turtle.Screen()
tela.title("Fome bateu, aqui resolveu!")
tela.setup(900, 700)
tela.bgcolor("#FFF0F5")
tela.tracer(0)

# CORES
ROSA = "#F7B6D2"
ROSA_ESCURO = "#D94F87"
ROSA_FORTE = "#C74378"
BRANCO = "#FFFFFF"
MARROM = "#75445B"

# CANETA DE DESENHO
caneta = turtle.Turtle()
caneta.hideturtle()
caneta.speed(0)
caneta.penup()

# ==========================================
# GIF
# ==========================================

# Coloque o GIF na mesma pasta do arquivo Python.
# Troque o nome abaixo pelo nome do seu arquivo.
NOME_GIF = "ddc826e5d2422d7f4160ded0287e1f51"
caminho_gif = Path(__file__).parent / NOME_GIF

imagem = turtle.Turtle()
imagem.penup()
imagem.speed(0)
imagem.hideturtle()

gif_disponivel = False

try:
    if caminho_gif.exists():
        tela.addshape(str(caminho_gif))
        imagem.shape(str(caminho_gif))
        gif_disponivel = True
    else:
        print("GIF nao encontrado:", caminho_gif)
except (turtle.TurtleGraphicsError, OSError) as erro:
    print("Erro ao carregar GIF:", erro)

# ==========================================
# BANCO DE RECEITAS
# ==========================================

receitas = {
    "Bolos": {
        "Bolo de chocolate": {
            "ingredientes": [
                "2 xicaras de farinha de trigo",
                "1 xicara de acucar",
                "1 xicara de chocolate em po",
                "2 ovos",
                "1 xicara de leite",
                "1 colher de fermento"
            ],
            "preparo": [
                "Misture a farinha, o acucar e o chocolate.",
                "Adicione os ovos e o leite.",
                "Coloque o fermento por ultimo.",
                "Asse a 180 graus por 35 a 40 minutos."
            ]
        },
        "Bolo de cenoura": {
            "ingredientes": [
                "2 cenouras",
                "2 ovos",
                "1/2 xicara de oleo",
                "2 xicaras de farinha",
                "1 xicara de acucar",
                "1 colher de fermento"
            ],
            "preparo": [
                "Bata a cenoura, os ovos e o oleo.",
                "Misture com os ingredientes secos.",
                "Acrescente o fermento.",
                "Asse a 180 graus por cerca de 35 minutos."
            ]
        },
        "Bolo de fuba": {
            "ingredientes": [
                "2 xicaras de fuba",
                "1 xicara de farinha",
                "1 xicara de acucar",
                "3 ovos e 1 xicara de leite",
                "1 colher de fermento"
            ],
            "preparo": [
                "Misture os ingredientes.",
                "Acrescente o fermento.",
                "Coloque em uma forma untada.",
                "Asse a 180 graus por 35 a 40 minutos."
            ]
        }
    },

    "Doces": {
        "Brigadeiro": {
            "ingredientes": [
                "1 lata de leite condensado",
                "2 colheres de chocolate em po",
                "1 colher de manteiga",
                "Chocolate granulado"
            ],
            "preparo": [
                "Misture tudo em uma panela.",
                "Mexa em fogo baixo ate desgrudar.",
                "Espere esfriar.",
                "Enrole e passe no granulado."
            ]
        },
        "Beijinho": {
            "ingredientes": [
                "1 lata de leite condensado",
                "100 g de coco ralado",
                "1 colher de manteiga"
            ],
            "preparo": [
                "Misture os ingredientes na panela.",
                "Mexa em fogo baixo ate desgrudar.",
                "Espere esfriar e enrole com coco."
            ]
        },
        "Mousse de limao": {
            "ingredientes": [
                "1 lata de leite condensado",
                "1 caixa de creme de leite",
                "Suco de 2 limoes"
            ],
            "preparo": [
                "Bata tudo no liquidificador.",
                "Coloque em um recipiente.",
                "Leve a geladeira por 2 a 3 horas."
            ]
        }
    },

    "Salgados": {
        "Pao de queijo": {
            "ingredientes": [
                "2 xicaras de polvilho",
                "1 xicara de queijo ralado",
                "1 ovo",
                "1/2 xicara de leite",
                "2 colheres de oleo e sal"
            ],
            "preparo": [
                "Misture todos os ingredientes.",
                "Faca bolinhas e coloque em uma forma.",
                "Asse a 180 graus por 25 a 30 minutos."
            ]
        },
        "Pizza de frigideira": {
            "ingredientes": [
                "1 xicara de farinha de trigo",
                "1/2 xicara de agua",
                "1 colher de azeite",
                "Sal, molho de tomate e queijo"
            ],
            "preparo": [
                "Misture farinha, agua, azeite e sal.",
                "Abra a massa e doure na frigideira.",
                "Adicione molho e queijo.",
                "Tampe ate o queijo derreter."
            ]
        },
        "Pastel de queijo": {
            "ingredientes": [
                "Massa de pastel pronta",
                "Queijo mussarela",
                "Oleo para fritar"
            ],
            "preparo": [
                "Coloque o queijo sobre a massa.",
                "Feche e aperte as bordas.",
                "Frite com ajuda de um adulto ate dourar."
            ]
        }
    },

    "Bebidas": {
        "Vitamina de banana": {
            "ingredientes": [
                "1 banana",
                "1 copo de leite",
                "1 colher de aveia (opcional)"
            ],
            "preparo": [
                "Coloque os ingredientes no liquidificador.",
                "Bata ate ficar cremoso.",
                "Sirva gelado."
            ]
        },
        "Limonada": {
            "ingredientes": [
                "2 limoes",
                "500 ml de agua",
                "Acucar e gelo a gosto"
            ],
            "preparo": [
                "Esprema os limoes.",
                "Misture com agua e acucar.",
                "Adicione gelo e sirva."
            ]
        },
        "Chocolate quente": {
            "ingredientes": [
                "2 xicaras de leite",
                "2 colheres de chocolate em po",
                "1 colher de acucar",
                "1 colher de amido de milho"
            ],
            "preparo": [
                "Misture os ingredientes em uma panela.",
                "Mexa em fogo baixo ate engrossar.",
                "Sirva com cuidado."
            ]
        }
    },

    "Receitas rapidas": {
        "Sanduiche natural": {
            "ingredientes": [
                "2 fatias de pao",
                "Frango desfiado ou queijo",
                "Alface e tomate",
                "Requeijao"
            ],
            "preparo": [
                "Passe requeijao no pao.",
                "Adicione o recheio e os vegetais.",
                "Feche o sanduiche e sirva."
            ]
        },
        "Omelete": {
            "ingredientes": [
                "2 ovos",
                "Queijo picado",
                "Sal e temperos a gosto"
            ],
            "preparo": [
                "Bata os ovos e adicione os temperos.",
                "Misture o queijo.",
                "Cozinhe em frigideira untada ate ficar firme."
            ]
        },
        "Crepioca": {
            "ingredientes": [
                "1 ovo",
                "2 colheres de tapioca",
                "Queijo ou outro recheio"
            ],
            "preparo": [
                "Misture o ovo e a tapioca.",
                "Coloque em uma frigideira untada.",
                "Doure dos dois lados e adicione o recheio."
            ]
        }
    }
}

# ==========================================
# FUNCOES DE DESENHO
# ==========================================

botoes = []

def escrever(x, y, texto, tamanho=14,
             cor=MARROM, estilo="normal"):
    caneta.penup()
    caneta.goto(x, y)
    caneta.color(cor)
    caneta.write(
        texto,
        align="center",
        font=("Arial", tamanho, estilo)
    )

def retangulo(x, y, largura, altura, cor):
    caneta.penup()
    caneta.goto(x - largura / 2, y - altura / 2)
    caneta.setheading(0)
    caneta.color(cor)
    caneta.pendown()
    caneta.begin_fill()

    for _ in range(2):
        caneta.forward(largura)
        caneta.left(90)
        caneta.forward(altura)
        caneta.left(90)

    caneta.end_fill()
    caneta.penup()

def botao(x, y, largura, altura, texto, acao):
    retangulo(x, y, largura, altura, ROSA)
    escrever(x, y - 7, texto, 13, MARROM, "bold")

    botoes.append({
        "x1": x - largura / 2,
        "x2": x + largura / 2,
        "y1": y - altura / 2,
        "y2": y + altura / 2,
        "acao": acao
    })

def limpar_tela():
    caneta.clear()
    botoes.clear()

def titulo():
    escrever(-40, 290, "FOME BATEU,", 27, ROSA_ESCURO, "bold")
    escrever(-40, 252, "AQUI RESOLVEU!", 24, ROSA_FORTE, "bold")

def atualizar():
    tela.update()

# ==========================================
# MENU PRINCIPAL
# ==========================================

def inicio():
    limpar_tela()
    titulo()

    escrever(0, 205, "Seu livro de receitas favorito!",
             16, MARROM)

    if gif_disponivel:
        imagem.goto(345, 215)
        imagem.showturtle()
    else:
        escrever(345, 205, "SEM GIF", 12, ROSA_ESCURO)

    botao(-170, 125, 270, 50, "Bolos",
          lambda: mostrar_receitas("Bolos"))

    botao(170, 125, 270, 50, "Doces",
          lambda: mostrar_receitas("Doces"))

    botao(-170, 55, 270, 50, "Salgados",
          lambda: mostrar_receitas("Salgados"))

    botao(170, 55, 270, 50, "Bebidas",
          lambda: mostrar_receitas("Bebidas"))

    botao(0, -15, 300, 50, "Receitas rapidas",
          lambda: mostrar_receitas("Receitas rapidas"))

    retangulo(0, -145, 650, 90, BRANCO)
    escrever(0, -130, "Escolha uma categoria e descubra",
             15, ROSA_ESCURO, "bold")
    escrever(0, -155, "uma receita deliciosa para fazer!",
             14, MARROM)

    escrever(0, -285, "Feito com carinho e uma pitada de amor!",
             13, ROSA_ESCURO)

    atualizar()

# ==========================================
# LISTA DE RECEITAS
# ==========================================

def mostrar_receitas(categoria):
    limpar_tela()
    imagem.hideturtle()
    titulo()

    escrever(0, 195, "Categoria: " + categoria,
             19, ROSA_FORTE, "bold")
    escrever(0, 160, "Escolha uma receita:",
             15, MARROM)

    nomes = list(receitas[categoria].keys())

    for i, nome in enumerate(nomes):
        y = 100 - i * 70

        botao(
            0, y, 360, 48, nome,
            lambda c=categoria, n=nome:
                mostrar_detalhes(c, n)
        )

    botao(-320, -285, 150, 45, "Voltar ao inicio", inicio)

    atualizar()

# ==========================================
# DETALHES DA RECEITA
# ==========================================

def mostrar_detalhes(categoria, nome):
    limpar_tela()
    imagem.hideturtle()
    titulo()

    escrever(0, 195, nome, 20, ROSA_FORTE, "bold")

    receita = receitas[categoria][nome]

    escrever(-190, 145, "INGREDIENTES",
             14, ROSA_ESCURO, "bold")

    y = 115
    for ingrediente in receita["ingredientes"]:
        escrever(-190, y, "- " + ingrediente, 11, MARROM)
        y -= 23

    escrever(190, 145, "MODO DE PREPARO",
             13, ROSA_ESCURO, "bold")

    y = 115
    for numero, passo in enumerate(receita["preparo"], start=1):
        escrever(190, y, str(numero) + ". " + passo,
                 10, MARROM)
        y -= 43

    botao(-320, -285, 150, 45, "Voltar",
          lambda: mostrar_receitas(categoria))

    botao(320, -285, 150, 45, "Inicio", inicio)

    atualizar()

# ==========================================
# CLIQUES NOS BOTOES
# ==========================================

def clique(x, y):
    for b in reversed(botoes):
        if (
            b["x1"] <= x <= b["x2"]
            and b["y1"] <= y <= b["y2"]
        ):
            b["acao"]()
            return

tela.onclick(clique)

# ==========================================
# INICIAR O PROGRAMA
# ==========================================

inicio()
turtle.done()

