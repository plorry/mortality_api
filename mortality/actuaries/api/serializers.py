from rest_framework import serializers
from actuaries.models import Actuary


class ActuarySerializer(serializers.ModelSerializer):


    class Meta:
        model = Actuary
        fields = ('year', 'age', 'mx', 'qx', 'ax', 'lx', 'dx',
            'Lx', 'Tx', 'ex')
