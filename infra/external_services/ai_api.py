import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def ask_question(question: str) -> str:
    context = """
A FURIA Esports é uma organização brasileira de esports fundada em agosto de 2017 por André Akkari, Jaime Pádua e Cris Guedes. Inicialmente focada em Counter-Strike, a FURIA expandiu suas operações e, atualmente, compete em diversas modalidades, incluindo:​
Wikipedia+3Meio e Mensagem+3Liquipedia+3

    Counter-Strike 2 (CS2)

    League of Legends (LoL)

    VALORANT

    Rocket League

    Rainbow Six: Siege

    Apex Legends

    FURIA FC (FIFA/EA Sports FC)​
    esports.gg+1Wikipédia, a enciclopédia livre+1
    ESPN.com+1Wikipedia+1
    esports.gg+9Wikipédia, a enciclopédia livre+9Wikipedia+9
    Liquipedia+2Wikipedia+2Wikipédia, a enciclopédia livre+2
    Esports Charts

A organização é reconhecida por seu estilo de jogo agressivo e por representar o Brasil em competições internacionais. Além do sucesso competitivo, a FURIA se destaca como um movimento sociocultural, promovendo valores como garra, estratégia e inovação.​
FURIA

Principais conquistas:

    Participações de destaque em torneios internacionais de CS:GO, como o PGL Major Stockholm 2021, IEM Rio Major 2022 e BLAST.tv Paris Major 2023. ​
    Wikipedia – Die freie Enzyklopädie+3Esports Charts+3Red Bull+3

Colaborações e parcerias:

    Parceria com a Adidas, resultando em uma linha de roupas e acessórios exclusivos. ​
    FURIA

Informações adicionais:

    Site oficial: https://www.furia.gg

    Perfil no X (antigo Twitter): https://x.com/furia​
    X (formerly Twitter)

"""
    prompt = f"{context}\n\n{question}"

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "Não consegui entender.")
    except Exception as e:
        print(f"Erro ao consultar o modelo: {e}")
        return "Erro ao acessar a IA local."
