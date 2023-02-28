from todo_app.models import TodoList
from django.http.response import JsonResponse
from todo_app.serializers import TodoListSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json






@csrf_exempt
def todo_lists_handler(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.all()
        serializer = TodoListSerializer(todo_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe=False)
    

@csrf_exempt
def todo_list_handler(request, pk):
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            todo_list = TodoList.objects.get(id=pk)
            serializer = TodoListSerializer(data=data, instance=todo_list)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
        except TodoList.DoesNotExist:
            return JsonResponse({'message': 'Todo list not found'}, status=status.HTTP_404_NOT_FOUND, safe=False)

    elif request.method == 'PUT':
        data = 
    elif request.method == 'Delete':
        pass
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe=False)

# @csrf_exempt
# def todo_list_handler(request, pk):
#     if request.method == 'GET':
#         todo_list = TodoList.objects.get(id=pk)
#         serializer = TodoListSerializer(todo_list, many = False)
#         return JsonResponse (serializer.data, status=status.HTTP_404_NOT_FOUND, safe=False)
#     elif request.method == 'PUT':
#         pass
#     elif request.method == 'DELETE':
#         pass
#     else:
#         return JsonResponse({'message': 'Request is not supported'})
        
    
    


@csrf_exempt
def todo_list_handler(request, pk):
    result = get_todo(pk)
    if result['todo'] is None:
        return JsonResponse({'message': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND, safe=False)
        
    todo = result['todo']
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST, safe=False)
        
    else:
        return JsonResponse({'message': 'Request is not supported'}, safe = False)
