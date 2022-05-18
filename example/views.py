from django.views.generic import ListView

from example import models as example_models


class ReasonListView(ListView):
    model = example_models.Reason

    def get_queryset(self):
        queryset = super().get_queryset()
        # Use snowflake db
        queryset = queryset.using('snowflake_analytics')
        return queryset
