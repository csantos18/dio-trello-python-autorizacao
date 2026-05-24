import json
import os
import urllib.parse
import urllib.request


def get_required_env(name):
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(f"Variavel de ambiente obrigatoria nao encontrada: {name}")

    return value


def build_url(api_key, token):
    params = urllib.parse.urlencode({
        "key": api_key,
        "token": token,
    })

    return f"https://api.trello.com/1/members/me?{params}"


def main():
    api_key = get_required_env("TRELLO_API_KEY")
    token = get_required_env("TRELLO_TOKEN")
    url = build_url(api_key, token)

    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    print("Autenticacao realizada com sucesso.")
    print(f"Usuario: {data.get('username')}")
    print(f"Nome completo: {data.get('fullName')}")


if __name__ == "__main__":
    main()
