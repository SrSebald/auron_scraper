from ajefech_client import fetch_tournaments

if __name__ == "__main__":

    tournaments =  fetch_tournaments()

    print(type(tournaments))

    print(len(tournaments))

    print(tournaments[0]["id"])

    print(tournaments[0]["title"])



