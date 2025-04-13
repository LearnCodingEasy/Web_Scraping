from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


class ScrapeView(APIView):
    def get(self, request, format=None):
        # URL of the site from which the data will be pulled
        url = 'https://web-scraping-project.pages.dev/'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract address
            title = soup.find('h2').text if soup.find(
                'h2') else 'No title found'

            # Text extraction
            text = soup.find('p').text if soup.find('p') else 'No text found'
            description = soup.find('meta', {'name': 'description'})
            description = description['content'] if description else 'No description found'
            # Extract some data from div
            data_paragraphs = soup.find_all('p', class_='info')
            data = [p.text for p in data_paragraphs]
            return Response(
                {
                    'title': title,
                    'text': text,
                    'description': description,
                    'data': data
                }
            )
        else:
            return JsonResponse({'error': 'Failed to retrieve data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
