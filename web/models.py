from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255)

    whatsapp = models.CharField(
        max_length=32,
        help_text="994XXXXXXXXX formatında (başında + olmadan)",
        blank=True,
    )

    working_hours = models.CharField(max_length=120, blank=True)
    map_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    photo = models.ImageField(upload_to="branches/", blank=True, null=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120, help_text="Məs: Loqoped, Psixoloq, Defektoloq")
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    branch = models.ForeignKey("Branch", on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "full_name"]

    def __str__(self):
        return self.full_name
    
class Service(models.Model):
    name = models.CharField(max_length=120)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=40,
        blank=True,
        help_text="Məs: brain, speech, child (sonra ikon set seçəcəyik)",
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
    
from django.db import models

class SiteContact(models.Model):
    whatsapp_number = models.CharField(
        max_length=20,
        default="994558811339",
        help_text="Yalnız rəqəmlər. Məs: 994558811339 (başında + olmasın).",
    )
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # singleton: həmişə 1-ci rekord
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Site Contact (WA: {self.whatsapp_number})"


