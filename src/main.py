from ajefech_client import fetch_tournaments
from ajefech_client import normalize_tournament
from ajefech_client import normalize_text

if __name__ == "__main__":

    tournaments =  fetch_tournaments()

    #Prueba    funcion fecth_tournament
    """
    print(type(tournaments))

    print(len(tournaments))

    print(tournaments[0]["id"])

    print(tournaments[0]["title"])
    """
    """
    #Pruebas de normalización
    sample = tournaments[0]

    norm = normalize_tournament(sample)

    print(type(norm)) 

    print(norm["id"])

    print(norm["title"])

    print(norm.get("is_online"))

    print(norm.get("is_santiago"))

    #print(norm[0].get("is_online"))

    print(normalize_text(" Ñuñoa, Santiago "))
    print(normalize_text("Maipú"))
    print(normalize_text("Lichess.org"))

    from ajefech_client import fetch_tournaments, normalize_tournament
    """

    tournaments = fetch_tournaments()
    # ✅ 1) Crear norm_list (lista normalizada)
    norm_list = [normalize_tournament(t) for t in tournaments]

    # ✅ 2) Imprimir lo pedido
    print(type(norm_list))
    print(len(norm_list))
    print(sum(t["is_online"] for t in norm_list))
    print(sum(t["is_santiago"] for t in norm_list))

    # ✅ 3) Mostrar 3 torneos online (title + address)
    online = [t for t in norm_list if t["is_online"]]
    for t in online[:3]:
        print(t["title"], "|", t["address"])





