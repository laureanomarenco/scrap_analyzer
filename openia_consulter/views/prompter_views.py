from django.shortcuts import render
import requests
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')

@csrf_exempt
def prompt_openia(request):
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        return JsonResponse({'error': 'API key no encontrada'}, status=400)

    # Configurar los headers con la clave de API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    # Configurar el cuerpo de la solicitud (equivalente al JSON en tu curl)
    data = {
        "model": "gpt-4o-mini",  # Aquí estamos usando el modelo GPT-4
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7,
    }

    # URL de la API de OpenAI
    url = "https://api.openai.com/v1/chat/completions"

    try:
        # Hacer la solicitud POST a OpenAI
        response = requests.post(url, headers=headers, json=data)
        
        # Comprobar si la respuesta fue exitosa
        if response.status_code == 200:
            respuesta_data = response.json()  # Convertir la respuesta a JSON
            return JsonResponse(respuesta_data, safe=False)  # Devolver la respuesta como JSON
        else:
            # Si la respuesta no es exitosa, devolver un mensaje de error
            return JsonResponse({
                'error': 'Error al conectar con OpenAI',
                'details': response.json(),
            }, status=response.status_code)
    
    except Exception as e:
        # En caso de error en la solicitud (por ejemplo, problemas de red)
        return JsonResponse({'error': str(e)}, status=500)
