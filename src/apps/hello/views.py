from django.shortcuts import render


def hello(request):
    name = request.GET.get("name", "my friend")
    message = request.GET.get("message", "Это тестовое задание для Rekruto!")
    context = {"name": name, "message": message}
    return render(request, "hello/base.html", context)
