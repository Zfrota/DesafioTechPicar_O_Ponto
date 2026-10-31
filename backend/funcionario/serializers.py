from rest_framework import serializers

class FuncionarioSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    
    
class ContadorSerializer(serializers.Serializer):
    funcionario = FuncionarioSerializer()
    timestamp = serializers.DateTimeField()
    
