from rest_framework import viewsets


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message."""

        return Response({'message': 'Hello!'})
