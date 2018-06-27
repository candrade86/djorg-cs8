from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content')

class NoteViewset(viewsets.ModeViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()       

