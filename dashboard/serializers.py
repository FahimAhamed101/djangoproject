from rest_framework import serializers


class TaransactionSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Product
        fields = [ "id", "name", "description", "inventory", "price", "images", "uploaded_images"]