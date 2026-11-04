import io
import sys
import base64
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

EVALS_DIR = Path(__file__).resolve().parent
ASSETS_DIR = EVALS_DIR / "test_assets"
ASSETS_DIR.mkdir(exist_ok=True)


def create_image_01_sharp_math() -> str:
    """Gera uma imagem de questão nítida de cálculo e física com fórmulas e alternativas."""
    img = Image.new("RGB", (700, 360), color="#ffffff")
    draw = ImageDraw.Draw(img)

    # Borda sutil de folha de prova
    draw.rectangle([(10, 10), (690, 350)], outline="#cccccc", width=2)

    # Textos da questão
    lines = [
        "SIMULADO EDUCAMOB — FISICA (CINEMATICA)",
        "",
        "Questao 1. Um automovel desloca-se sobre uma rodovia retilinea de acordo",
        "com a seguinte funcao horaria da posicao:",
        "",
        "             S(t) = 30 + 15 * t   (com S em metros e t em segundos)",
        "",
        "Com base nessas informacoes, qual e a posicao inicial (S0) e a velocidade (v)?",
        "",
        "a) S0 = 15 m e v = 30 m/s",
        "b) S0 = 30 m e v = 15 m/s",
        "c) S0 = 45 m e v = 15 m/s",
        "d) S0 = 30 m e v = 45 m/s",
        "e) S0 = 0 m e v = 15 m/s"
    ]

    y = 25
    for line in lines:
        draw.text((30, y), line, fill="#111111")
        y += 20

    img_path = ASSETS_DIR / "img_01_sharp_math.png"
    img.save(img_path, format="PNG")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{b64}"


def create_image_02_graph() -> str:
    """Gera uma imagem de questão com gráfico cartesiano velocidade x tempo."""
    img = Image.new("RGB", (750, 420), color="#ffffff")
    draw = ImageDraw.Draw(img)

    draw.rectangle([(10, 10), (740, 410)], outline="#cccccc", width=2)

    draw.text((30, 25), "EXERCICIO DE FISICA — ANALISE GRAFICA", fill="#111111")
    draw.text((30, 50), "O grafico abaixo representa a velocidade v(t) de uma particula em MUV:", fill="#222222")

    # Desenha eixos cartesianos
    origin = (100, 260)
    # Eixo Y (v em m/s)
    draw.line([(100, 270), (100, 90)], fill="#333333", width=2)
    # Eixo X (t em s)
    draw.line([(90, 260), (380, 260)], fill="#333333", width=2)

    # Rótulos dos eixos
    draw.text((60, 85), "v (m/s)", fill="#000088")
    draw.text((385, 255), "t (s)", fill="#000088")

    # Marcas e valores no gráfico
    # v = 0 em t = 0
    # v = 20 em t = 4
    draw.line([(95, 120), (105, 120)], fill="#333333", width=2)
    draw.text((75, 115), "20", fill="#111111")

    draw.line([(320, 255), (320, 265)], fill="#333333", width=2)
    draw.text((315, 270), "4", fill="#111111")

    # Linhas tracejadas
    draw.line([(100, 120), (320, 120)], fill="#999999", width=1)
    draw.line([(320, 260), (320, 120)], fill="#999999", width=1)

    # Reta da velocidade (subindo de 0 a 20)
    draw.line([(100, 260), (320, 120)], fill="#cc0000", width=3)
    draw.ellipse([(97, 257), (103, 263)], fill="#cc0000")
    draw.ellipse([(317, 117), (323, 123)], fill="#cc0000")

    # Enunciado ao lado
    text_x = 420
    draw.text((text_x, 90), "Pergunta:", fill="#111111")
    draw.text((text_x, 115), "A partir do grafico ao lado,", fill="#222222")
    draw.text((text_x, 135), "determine o valor da aceleracao", fill="#222222")
    draw.text((text_x, 155), "escalar media da particula.", fill="#222222")

    draw.text((text_x, 190), "a) 2 m/s^2", fill="#222222")
    draw.text((text_x, 215), "b) 4 m/s^2", fill="#222222")
    draw.text((text_x, 240), "c) 5 m/s^2", fill="#222222")
    draw.text((text_x, 265), "d) 10 m/s^2", fill="#222222")
    draw.text((text_x, 290), "e) 20 m/s^2", fill="#222222")

    img_path = ASSETS_DIR / "img_02_graph.png"
    img.save(img_path, format="PNG")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{b64}"


def create_image_03_cropped_incomplete() -> str:
    """Gera uma imagem de questão deliberadamente cortada/incompleta para teste de ambiguidade."""
    img = Image.new("RGB", (650, 160), color="#ffffff")
    draw = ImageDraw.Draw(img)

    # Borda cortada abruptamente na parte inferior
    draw.rectangle([(5, 5), (645, 155)], outline="#dddddd", width=1)

    draw.text((25, 20), "VESTIBULAR 2026 — FISICA — DINAMICA", fill="#111111")
    draw.text((25, 45), "Um bloco de massa m = 8 kg repousa sobre uma superficie plana.", fill="#222222")
    draw.text((25, 70), "Uma forca horizontal F e aplicada sobre o bloco, fazendo com que ele", fill="#222222")
    draw.text((25, 95), "acelere a uma taxa constante de 3 m/s^2. Sabendo que o atrito...", fill="#222222")
    draw.text((25, 120), "a) F = 14 N   b) F = 24 N   c) [FOTO CORTADA]", fill="#777777")

    # Linha irregular de rasgo/corte
    for x in range(0, 650, 20):
        draw.line([(x, 145), (x + 10, 155)], fill="#ff3333", width=2)
        draw.line([(x + 10, 155), (x + 20, 145)], fill="#ff3333", width=2)

    img_path = ASSETS_DIR / "img_03_cropped.png"
    img.save(img_path, format="PNG")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{b64}"


if __name__ == "__main__":
    b1 = create_image_01_sharp_math()
    b2 = create_image_02_graph()
    b3 = create_image_03_cropped_incomplete()
    print(f"Imagens de teste geradas com sucesso em: {ASSETS_DIR}")
    print(f"Img 1 length: {len(b1)} | Img 2 length: {len(b2)} | Img 3 length: {len(b3)}")
