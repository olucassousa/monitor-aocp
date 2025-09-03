import requests
from bs4 import BeautifulSoup

URLS = [
    "https://www.institutoaocp.org.br/concursos/status/novos",
    "https://www.institutoaocp.org.br/concursos/status/em-andamento",
    "https://www.institutoaocp.org.br/concursos/status/finalizados",
]

TERMS = [
    "ppmg",
    "polícia penal",
    "policia penal",
    "minas gerais",
    "distrito federal",
    "policia penal df",
]

def verificar_site():
    achados = []
    for url in URLS:
        try:
            r = requests.get(url, timeout=20)
            if r.status_code != 200:
                continue
            soup = BeautifulSoup(r.text, "html.parser")
            texto = soup.get_text(" ", strip=True).lower()
            encontrados = [t for t in TERMS if t in texto]
            if encontrados:
                achados.append({"url": url, "termos": encontrados})
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")
    return achados

if __name__ == "__main__":
    resultados = verificar_site()
    if resultados:
        print("⚠️ Termos encontrados:")
        for r in resultados:
            print(f"- {r['url']} → {', '.join(r['termos'])}")
    else:
        print("❌ Nenhuma menção encontrada.")
