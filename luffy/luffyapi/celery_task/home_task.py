from .celery import app


@app.task
def banner_update():
    from home import serializaer
    from home import models
    from django.conf import settings
    from django.core.cache import cache
    queryset_banner = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[
                      :settings.BANNER_COUNTER]
    serializaer_banner = serializaer.BannerModelSerializer(instance=queryset_banner, many=True)
    print(serializaer_banner.data)
    for banner in serializaer_banner.data:
        banner['img'] = settings.URL + banner['img']
        cache.set('banner_list', serializaer_banner.data)

    # import time
    # time.sleep(1)
    # print(cache.get('banner_list'))
    return True
