import logging
import traceback
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('oauth_debug')
allauth_logger = logging.getLogger('allauth')

class OAuthDebugMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if 'google' in request.path:
            logger.error(f"🔴 EXCEPTION in google callback!")
            logger.error(f"🔴 Exception type: {type(exception).__name__}")
            logger.error(f"🔴 Exception message: {str(exception)}")
            logger.error(f"🔴 Traceback: {traceback.format_exc()}")
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'google' in request.path and 'callback' in request.path:
            logger.debug(f"🔵 CALLBACK TRIGGERED")
            logger.debug(f"🔵 Code from Google: {request.GET.get('code', 'NO CODE!')}")
            logger.debug(f"🔵 User: {request.user}")
            logger.debug(f"🔵 Session: {request.session.session_key}")
        return None

    def process_response(self, request, response):
        if 'google' in request.path and 'callback' in request.path:
            logger.debug(f"🟢 Callback Response: {response.status_code}")
        return response
