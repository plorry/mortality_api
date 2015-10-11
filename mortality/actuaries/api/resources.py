from rest_framework import viewsets
from actuaries.api.renderers import AttributionRenderer
from actuaries.models import Actuary
from actuaries.api.serializers import ActuarySerializer


class ActuaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actuary.objects.all()
    serializer_class = ActuarySerializer
    renderer_classes = (AttributionRenderer,)
    paginate_by = 50

    def get_queryset(self, *args, **kwargs):
        queryset = super(ActuaryViewSet, self).get_queryset(*args, **kwargs)
        params = self.request.query_params
        query_dict = {key: value for (key, value) in params.items()
            if key in Actuary._meta.get_all_field_names()}
        queryset = queryset.filter(**query_dict)

        return queryset
