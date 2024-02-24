from rest_framework.response import Response
from rest_framework.views import APIView

import random

class Provider(APIView):
    def get(self, request, format=None):
        min_value = request.GET.get('min', 0)
        max_value = request.GET.get('max', 10000)
        
        # Ensure the values are integers
        try:
            min_value = int(min_value)
            max_value = int(max_value)
        except ValueError:
            return Response({"error": "Invalid min or max value. Please provide integer values."}, status=400)
        
        # Check if min_value is greater than max_value
        if min_value > max_value:
            return Response({"error": "min value should not be greater than max value."}, status=400)
        
        # Generate a random number between min_value and max_value
        random_number = random.randint(min_value, max_value)
        
        return Response({"random_number": random_number})
