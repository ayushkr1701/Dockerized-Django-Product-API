from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from typing import Any, Dict, Union
from .models import Product
import json

@csrf_exempt
def create_product(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        try:
            data: Dict[str, Any] = json.loads(request.body)
            product: Product = Product.objects.create(
                name=data['name'],
                category=data['category'],
                price=data['price']
            )
            return JsonResponse({'message': 'Product created successfully', 'id': product.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_product_by_id(request: HttpRequest, product_id: int) -> JsonResponse:
    try:
        product: Product = Product.objects.get(pk=product_id)
        data: Dict[str, Union[int, str, float]] = {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def get_all_products(request: HttpRequest) -> JsonResponse:
    products: QuerySet[Product] = Product.objects.all()
    data: List[Dict[str, Union[int, str, float]]] = [{'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price} for product in products]
    return JsonResponse(data, safe=False)

@csrf_exempt
def update_product(request: HttpRequest, product_id: int) -> JsonResponse:
    try:
        product: Product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'PUT':
        try:
            data: Dict[str, Any] = json.loads(request.body)
            product.name = data.get('name', product.name)
            product.category = data.get('category', product.category)
            product.price = data.get('price', product.price)
            product.save()
            return JsonResponse({'message': 'Product updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_product(request: HttpRequest, product_id: int) -> JsonResponse:
    try:
        product: Product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'DELETE':
        try:
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
