import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt


class ChatterBotAppView(TemplateView):
    template_name = 'index3.html'


class DocumentoinFileView(TemplateView):
    template_name = 'documentation.html'

    
    
@csrf_exempt
def test(request):
    if( request.method == "POST" ):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        input_data = request.POST.get('statement')

        response = chatterbot.get_response(input_data)
        conf = response.confidence

        print(response)

        response_data = response.serialize()
        response_data['confidence'] = conf
        if( conf <= .8 ):
            response_data['OD'] = response_data['text']
            response_data['text'] = "I don't understand your question!!"

        return JsonResponse(response_data, status=200)
    else:
        chatterbot = ChatBot(**settings.CHATTERBOT)
        input_data = request.POST.get('statement')
        print(input_data)
        response = chatterbot.get_response(input_data)
        response_data = response.serialize()
        return JsonResponse(response_data, status=200)

class ChatterBotApiView(View):    
    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):        
        input_data = request.POST.get('statement')        

        print(input_data)

        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()
        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
