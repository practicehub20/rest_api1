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
                message = dict_to_json(serialize_obj.data)
            except ProductModel.DoesNotExist:
                error = {
                    'error': 'Your requested IDNO does not match.'
                }
                message = dict_to_json(error)
        else:
            models_obj = ProductModel.objects.all()
            serialize_objs = ProductSerializers(models_obj, many=True)
            message = dict_to_json(serialize_objs.data)
        return HttpResponse(message, content_type='application/json')

    def post(self,request):
        dict_data = json_to_dict(request.body)
        serializer_obj = ProductSerializers(data=dict_data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            success = {
                'info' : 'Data saved successfully'
            }
            message = dict_to_json(success)
        else:
            message = dict_to_json(serializer_obj.errors)
        return HttpResponse(message, content_type='application/json')


