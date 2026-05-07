from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'PaginaPrincipal.html')


def aluguel_page(request):
    return render(request, 'Aluguel.html')


def pagar_foto_unica(request):
    return render(request, 'PagarFotoUnica')


def pagar_foto_grupo(request):
    return render(request, 'PagarFotoGrupo')


def contato_page(request):
    return render(request, 'Contato.html')


def email_page(request):
    return render(request, 'Email.html')


def politica_page(request):
    return render(request, 'politica.html')