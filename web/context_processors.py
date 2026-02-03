from .models import SiteContact

def site_contact(request):
    contact, _ = SiteContact.objects.get_or_create(id=1)
    return {"site_contact": contact}