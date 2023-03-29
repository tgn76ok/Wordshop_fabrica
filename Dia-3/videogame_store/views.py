from django.http import JsonResponse


def jogos(resquest):
    if resquest.method == "GET":

        jogo = {
            "nome": "cs2",
            "genero": "cs"
        }
    return JsonResponse(jogo)
