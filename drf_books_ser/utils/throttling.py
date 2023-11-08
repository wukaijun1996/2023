from rest_framework.throttling import ScopedRateThrottle, SimpleRateThrottle


class MyThrottle(SimpleRateThrottle):
    scope = 'luffy'

    def get_cache_key(self, request, view):
        print(request.META.get('REMOTE_ADDR'))
        return request.META.get('REMOTE_ADDR')
