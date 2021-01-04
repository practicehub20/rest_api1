from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from app1.common import json_to_dict, dict_to_json
from app1.models import ProductModel
from app1.serializers import ProductSerializers
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class ProductView(View):
    def get(self, request):
        json_data = request.body
        if json_data:
            try:
                dict_data = json_to_dict(json_data)
                model_object = ProductModel.objects.get(idno=dict_data['idno'])
                serialize_obj = ProductSerializers(model_object)
                result = serialize_obj.data
            except ProductModel.DoesNotExist:
                result = {
                    'error': 'Your requested IDNO does not match.'
                }
        else:
            models_obj = ProductModel.objects.all()
            serialize_objs = ProductSerializers(models_obj, many=True)
            result = serialize_objs.data
        message = dict_to_json(result)
        return HttpResponse(message, content_type='application/json')

    def post(self,request):
        dict_data = json_to_dict(request.body)
        serializer_obj = ProductSerializers(data=dict_data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            result = {
                'info' : 'Data saved successfully'
            }
        else:
            result = serializer_obj.errors
        message = dict_to_json(result)
        return HttpResponse(message, content_type='application/json')

    def put(self,request):
        dict_data = json_to_dict(request.body)
        try:
            model_object = ProductModel.objects.get(idno=dict_data['idno'])
            serializer_obj = ProductSerializers(model_object, dict_data, partial=True)
            if serializer_obj.is_valid():
                serializer_obj.save()
                result = {
                    'info' : 'Resource updated successfully.'
                }
            else:
                result = serializer_obj.errors
        except ProductModel.DoesNotExist:
            result = {
                'error' : 'Your requested IDNO does not match.'
            }
        message = dict_to_json(result)
        return HttpResponse(message, content_type='application/json')

    def delete(self, request):
        dict_data = json_to_dict(request.body)
        try:
            model_object = ProductModel.objects.get(idno=dict_data['idno'])
            model_object.delete()
            result = {
                'info' : 'Resourse deleted successfully.'
            }
        except ProductModel.DoesNotExist:
            result = {
                'error' : 'Your requested IDNO does not match.'
            }
        message = dict_to_json(result)
        return HttpResponse(message, content_type='application/json')



