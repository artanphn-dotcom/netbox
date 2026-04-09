import os
import sys

import django

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netbox.settings')
django.setup()

from dcim.models import Device, Rack, Site
from ipam.models import IPAddress, Prefix, VLAN
from tenancy.models import Tenant

site = Site.objects.filter(name='Example Campus').first()

print(f"sites={Site.objects.filter(name='Example Campus').count()}")
print(f"tenants={Tenant.objects.filter(name='Example Retail').count()}")
print(f"racks={Rack.objects.filter(site=site).count() if site else 0}")
print(f"devices={Device.objects.filter(name__startswith='sw-demo-').count()}")
print(f"vlans={VLAN.objects.filter(site=site).count() if site else 0}")
print(f"prefixes={Prefix.objects.filter(scope_id=site.pk).count() if site else 0}")
print(f"ips={IPAddress.objects.filter(dns_name__icontains='example-campus.local').count()}")
