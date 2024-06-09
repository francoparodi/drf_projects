import json
from rest_framework import generics, status

from .models import Solution
from .serializers import SolutionSerializer, UploadedFileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class SolutionListCreateView(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer


class SolutionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    partial = True


class SolutionDeleteView(generics.DestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Solution"))
    
    
class SolutionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer


class FileUploadView(APIView):
    def post(self, request):
        content = request.data.get('content')
        if content:
            try:
                content_str = content.read().decode('utf-8')
                json_data = json.loads(content_str)
                serializer = UploadedFileSerializer(data={'content': json_data})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'Missing content'}, status=status.HTTP_400_BAD_REQUEST)