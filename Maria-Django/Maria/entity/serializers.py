from rest_framework import serializers

from .models import GroupMember


class GroupMemberSerializer(serializers.ModelSerializer):
    """定义序列化器"""
    class Meta:
        model = GroupMember # 指定序列化从哪个模型映射字段
        fields = '__all__'
