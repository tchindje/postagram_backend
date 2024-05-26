from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    """
        Define fields that will be present in every serializer.
    """

    id = serializers.UUIDField(
        source='public_id',
        read_only=True,
        format='hex'
    )
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
