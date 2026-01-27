import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('oauth_debug')


@csrf_exempt
def debug_callback(request):
    """Debug endpoint za testiranje"""
    logger.debug(f"🔵 DEBUG CALLBACK")
    logger.debug(f"🔵 Path: {request.path}")
    logger.debug(f"🔵 Full URL: {request.build_absolute_uri()}")
    logger.debug(f"🔵 Code: {request.GET.get('code')}")

    return JsonResponse({
        'status': 'received',
        'code': request.GET.get('code'),
        'url': request.build_absolute_uri(),
    })
