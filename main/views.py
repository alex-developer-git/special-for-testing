from datetime import date
from typing import Any, Dict, List, Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Product


def home(request: HttpRequest):
    """
    Render the home page.
    """
    return render(request, 'main/home.html')


def about(request: HttpRequest):
    """
    Render the about page with company information.
    """
    company_description = (
        "is a leading force in the security industry, dedicated to delivering "
        "cutting-edge solutions that safeguard what matters most. We are committed to "
        "providing comprehensive protection and peace of mind, no matter the challenge."
    )
    company_html_text = (
        "Our mission is to deliver <strong>trusted security solutions</strong> "
        "with a focus on <em>reliability</em> and <em>innovation</em>."
    )
    return render(request, 'main/about.html',
                  {"last_updated": date.today(),
                   "company_description": company_description,
                   "company_html_text": company_html_text})


class ContactView(TemplateView):
    """
    Render the contact page.
    """
    template_name = 'main/contact.html'


class ServiceView(TemplateView):
    """
    Render services with optional category filtering.
    """
    template_name = 'main/service.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Build context data including services and filtering data.
        """
        context = super().get_context_data(**kwargs)
        services = [
            {"name": "Border Control", "category": "Security"},
            {"name": "Enhanced Situational Awareness", "category": "Intelligence"},
            {"name": "Cybersecurity", "category": "Cyber"},
            {"name": "Unmanned Technologies", "category": "Defense"},
            {"name": "Secure Communication", "category": "Communications"},
            {"name": "Counter-Intelligence", "category": "Intelligence"},
            {"name": "Counter-Drone Technologies", "category": "Defense"},
            {"name": "RF Jamming", "category": "Electronic Warfare"},
            {"name": "Social Media Intelligence", "category": "Intelligence"},
            {"name": "Lawful Interception", "category": "Security"}, ]

        selected_category = self.request.GET.get("category")
        if selected_category:
            services = [s for s in services if s["category"] == selected_category]
        categories = sorted({s["category"] for s in services})
        context["services"] = services
        context["categories"] = categories
        context["selected_category"] = selected_category
        context["services_count"] = len(services)
        return context

def test_func_one(request: HttpRequest) -> HttpResponse:
    product = Product(name="Telephone", price=199.99, stock=10)
    product.save()

def test_func_two(request: HttpRequest) -> HttpResponse:
    product = Product.objects.create(name="Telephone", price=199.99, stock=10)


def reader(request: HttpRequest) -> HttpResponse:
    all_product = Product.objects.all()
    product = Product.objects.get(id=1)
    products = Product.objects.filter(price__gte=400)

def update(request: HttpRequest) -> HttpResponse:
    product = Product.objects.get(id=1)
    product.price = 849.99
    product.save()

def delete(request: HttpRequest) -> HttpResponse:
    product = Product.objects.get(id=1)
    product.delete()

