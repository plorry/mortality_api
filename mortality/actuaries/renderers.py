from rest_framework.renderers import JSONRenderer
from actuaries.constants import Attribution


class AttributionRenderer(JSONRenderer):
    """
    Include attribution with each response
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = data
        response_data.update({'attribution': Attribution.ATTRIBUTION})

        response = super(AttributionRenderer, self).render(response_data, accepted_media_type, renderer_context)
        return response
