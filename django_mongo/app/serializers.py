from rest_framework_mongoengine import serializers


from .models import Tool, ToolInput

# class ToolInputSerializer(serializers.Serializer):
#     class Meta:
#         model = ToolInput
#         fields = '__all__'

class ToolSerializer(serializers.DocumentSerializer):
    # inputs = ToolInputSerializer(many=True)

    class Meta:
        model = Tool
        fields = ('label', 'description', 'inputs')
