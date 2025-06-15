from shop.models import Category, Product, Subcategory, Manufacturer
from django.db.models import Q

class CatalogService:
    def getCategories():
        return {"categories": Category.objects.all()}

    def getCategory(category_id):
        category = Category.objects.get(pk=category_id)
        return category

    def getSubcategory(subcategory_id):
        subcategory = Subcategory.objects.get(pk=subcategory_id)
        return subcategory

    def getProduct(product_id):
        product = Product.objects.get(pk=product_id)
        return product

    def getManufacturers():
        return Manufacturer.objects.all()

    def getFilteredProducts(category, subcategory_id, manufacturer_id):
        try:
            subcategory = int(subcategory_id)
            subcategory = None if subcategory < 0 else subcategory
        except:
            subcategory = None

        try:
            manufacturer = int(manufacturer_id)
            manufacturer = None if manufacturer < 0 else manufacturer
        except:
            manufacturer = None

        q = Q()
        if subcategory:
            subcategory = Subcategory.objects.get(pk=subcategory)
            q &= Q(subcategory=subcategory)
        if manufacturer:
            manufacturer = Manufacturer.objects.get(pk=manufacturer)
            q &= Q(manufacturer=manufacturer)

        products = Product.objects.filter(q)
        return { "products": products, "subcategory": subcategory, "manufacturer": manufacturer }
