from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Author
from django.views.decorators.csrf import csrf_exempt
import json

class AuthorREST(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, id=None):

        if id is None:
            data = []
            for author in Author.objects.all():
                data_author = {'id': author.id,
                               'name': author.name,
                               'email':author.email}
                data.append(data_author)
        else:
            author = Author.object.filter(id=id)
            if author:
                author = author.first()
                data = {'id': author.id,
                        'name': author.name,
                        'email':author.email}
            else:
                return JsonResponse ({'error': f'Автора с id={id} не найдено!'},
                                        status = 404,
                                        json_dumps_params = {"ensure_ascii": False,
                                                               "indent": 4})
        return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False,
                                                               "indent": 4})
    def post(self, request):
        try:
            data = json.loads(request.body)
            author = Author(name=data['name'], email=data['email'])
            author.clean_fields()
            author.save()
            response_data = {
                'message': f' Автор успешно создан',
                'id': author.id,
                'name': author.name,
                'email': author.email
            }
            return JsonResponse(response_data, status=201,
                                json_dumps_params={"ensure_ascii": False,
                                                   "indent": 4}
                                )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400,
                                json_dumps_params={"ensure_ascii": False,
                                                   "indent": 4}
                                )

# Create your views here.
