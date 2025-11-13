import requests

if __name__ == "__main__":
    lugar = "Puebla"
    r = requests.get(f"http://wttr.in/{lugar}?format=3")
    print(r.text)