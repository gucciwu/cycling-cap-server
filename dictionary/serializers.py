from .models import Dictionary
from base.serializers import BaseHyperlinkedModelSerializer


class DictionarySerializer(BaseHyperlinkedModelSerializer):
    class Meta(BaseHyperlinkedModelSerializer.Meta):
        model = Dictionary

    def create(self, validated_data):
        return Dictionary.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dict_entry = validated_data.get('dict_entry', instance.entry)
        instance.dict_key = validated_data.get('dict_key', instance.key)
        instance.dict_value = validated_data.get('dict_value', instance.value)
        instance.dict_remark = validated_data.get('dict_remark', instance.value)
        instance.save()
        return instance



