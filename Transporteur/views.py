from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Product, DeliveryTime, StorageCondition, TransportAvailability, Transporter, Cargo

def transporteur_view(request):
    products = Product.objects.all()
    delivery_times = DeliveryTime.objects.all()
    storage_conditions = StorageCondition.objects.all()
    transport_availabilities = TransportAvailability.objects.all()
    transporters = Transporter.objects.all()
    cargos = Cargo.objects.all()

    # Sérialisation des objets en JSON
    products_json = serialize('json', products)
    delivery_times_json = serialize('json', delivery_times)
    storage_conditions_json = serialize('json', storage_conditions)
    transport_availabilities_json = serialize('json', transport_availabilities)
    transporters_json = serialize('json', transporters)
    cargos_json = serialize('json', cargos)

    # Création du dictionnaire JSON
    data = {
        'products': products_json,
        'delivery_times': delivery_times_json,
        'storage_conditions': storage_conditions_json,
        'transport_availabilities': transport_availabilities_json,
        'transporters': transporters_json,
        'cargos': cargos_json,
    }

    # Retourne le dictionnaire JSON comme réponse
    return JsonResponse(data, safe=False)
