
from django.shortcuts import render


from ..models import Service


def services(request):

    services_data = Service.objects.all()

    return render(
        request, 'services/index.html',
        {
            "services":
                services_data
        }
    )


def service(request, **kwargs):
    service_data = Service.objects.get(**kwargs)
    maintenance = service_data.maintenance.all()
    return render(
        request, 'services/details.html',
        {
            "service":
                service_data,
            "maintenance_list":
                maintenance
        }
    )
