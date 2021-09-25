import django_filters

from shopify.models import Order


class OrderFilter(django_filters.FilterSet):
    created_after = django_filters.CharFilter(method="get_created_time_after")
    created_before = django_filters.CharFilter(method="get_created_time_before")

    class Meta:
        model = Order
        fields = ["created_after", "created_before"]

    def get_created_time_before(self, queryset, name, value):
        from django.utils.dateparse import parse_date, parse_datetime
        try:
            value_parsed = parse_datetime(value)
        except:
            pass
        if not value_parsed:
            try:
                import datetime
                value_parsed = parse_date(value)
                value_parsed = datetime.datetime.combine(value_parsed, datetime.time(23, 59, 59))
            except Exception as e:
                pass
        if value_parsed:
            return queryset.filter(created_at__lte=value_parsed)
        return queryset

    def get_created_time_after(self, queryset, name, value):
        from django.utils.dateparse import parse_date, parse_datetime
        try:
            value_parsed = parse_datetime(value)
        except:
            pass
        if not value_parsed:
            try:
                value_parsed = parse_date(value)
            except Exception as e:
                pass
        if value_parsed:
            return queryset.filter(created_at__gte=value_parsed)
        return queryset