from django.http import JsonResponse

def estudante(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'John'
        }
        return JsonResponse(estudante)
