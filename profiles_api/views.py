from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function (get, post, pacth, put, delete)',
            'Is similar to a tradicional Django View',
            'Gives you the most control over you application logic',
            'Is mapped maually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
