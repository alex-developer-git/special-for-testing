from typing import Dict, Any
from django.http import HttpRequest
from django.conf import settings


def add_global_data(request: HttpRequest) -> Dict[str, Any]:
    """
    Add global site-related settings to the template context.
    Makes common configuration values available in all templates.
    """
    return {
        "site_name": getattr(settings, "SITE_NAME", None),
        "support_email": getattr(settings, "SUPPORT_EMAIL", None),
        "address": getattr(settings, "ADDRESS", None),
        "contact_number": getattr(settings, "CONTACT_NUMBER", None),
        "support_enabled": bool(getattr(settings, "SUPPORT_EMAIL", "")),
    }