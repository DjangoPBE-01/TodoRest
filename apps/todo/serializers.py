from rest_framework import serializers
from apps.todo.models import Category, Task


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')
        
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
        
class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)



class TaskListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        
        
class ExampleSerializer21(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    hhhhh = serializers.CharField(max_length=100, required=False)
    
    birth_year = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    
    
    
    def validate(self, data):
        if data['name'] == 'Admin' and data['age'] < 18:
            raise serializers.ValidationError("Admin bo'lish uchun yosh 18 dan katta bo'lishi kerak.")
        return data
    
    
    
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Yosh manfiy bo'lishi mumkin emas.")
        return value
    
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email faqat @example.com bilan tugashi kerak.")
        return value
    
    
    def get_birth_year(self, obj):
        from datetime import datetime
        
        current_year = datetime.now().year
        
        return current_year - obj['age']
    
    
    def get_status(self, obj):
        if obj['age'] < 18:
            return "Minor"
        elif 18 <= obj['age'] < 65:
            return "Adult"
        else:
            return "Senior"
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['personal_info'] = {
            'name': representation['name'],
            'age': representation['age'],
            'email': representation['email']
        }
        
        representation['additional_info'] = {
            'birth_year': representation['birth_year'],
            'status': representation['status']
        }
        
        representation.pop('name')
        representation.pop('age')
        representation.pop('email')
        
        representation.pop('birth_year')
        representation.pop('status')
        representation.pop('hhhhh')
        
        return representation
    
    
    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        data = internal_value.copy()  # Create a copy of the internal value to modify
        
        data['name'] = "Jamshidbek"  # Example of modifying the name field before validation
            
        
        return data
    
    
    

