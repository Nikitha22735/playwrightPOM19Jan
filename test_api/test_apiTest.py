# from playwright.sync_api import sync_playwright
from playwright.sync_api import expect, Page, sync_playwright


def getApi(playwright: sync_playwright):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch()
        # context = browser.new_context()
    #     page = context.new_page()
    context = playwright.request.new_context()
    headerValues = {"Authorization": "bearer 12345", 
                    "User-Agent": "PostmanRuntime/7.51.1"}

    # headerValues = {"Authorization": {"Username":"nikitha", "Password":"123"}, 
    #                 "User-Agent": "PostmanRuntime/7.51.1"}
    response = context.get("https://dummyjson.com/products", headers=headerValues)
    # context.put(url)
    print(response.status)
    result = response.json()
   
    print(result["products"][0]["title"])

    assert response.status==200


def test_postApi(playwright: sync_playwright):
    context = playwright.request.new_context()
    headerValues = {"Authorization": "bearer 12345", 
                    "User-Agent": "PostmanRuntime/7.51.1"}
    body1 = {
            "description": "CK One by Calvin Klein is a classic unisex fragrance, known for its fresh and clean scent. It's a versatile fragrance suitable for everyday wear.",
            "category": "fragrances",
            "price": 49.99,
            "discountPercentage": 1.89,
            "stock": 29,
            "tags": [
                "fragrances",
                "perfumes"
            ],
            "brand": "Calvin Klein",
            "sku": "FRA-CAL-CAL-006",
            "weight": 7,
            "dimensions": {
                "width": 29.36,
                "height": 27.76,
                "depth": 20.72
            },
            "warrantyInformation": "1 week warranty",
            "shippingInformation": "Ships overnight",
            "availabilityStatus": "In Stock",
            "reviews": [
                {
                    "rating": 2,
                    "comment": "Very disappointed!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Layla Young",
                    "reviewerEmail": "layla.young@x.dummyjson.com"
                },
                {
                    "rating": 4,
                    "comment": "Fast shipping!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Daniel Cook",
                    "reviewerEmail": "daniel.cook@x.dummyjson.com"
                },
                {
                    "rating": 3,
                    "comment": "Not as described!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Jacob Cooper",
                    "reviewerEmail": "jacob.cooper@x.dummyjson.com"
                }
            ],
            "returnPolicy": "90 days return policy",
            "minimumOrderQuantity": 9,
            "meta": {
                "createdAt": "2025-04-30T09:41:02.053Z",
                "updatedAt": "2025-04-30T09:41:02.053Z",
                "barcode": "2451534060749",
                "qrCode": "https://cdn.dummyjson.com/public/qr-code.png"
            },
            "images": [
                "https://cdn.dummyjson.com/product-images/fragrances/calvin-klein-ck-one/1.webp",
                "https://cdn.dummyjson.com/product-images/fragrances/calvin-klein-ck-one/2.webp",
                "https://cdn.dummyjson.com/product-images/fragrances/calvin-klein-ck-one/3.webp"
            ],
            "thumbnail": "https://cdn.dummyjson.com/product-images/fragrances/calvin-klein-ck-one/thumbnail.webp"
        }
    response = context.post("https://dummyjson.com/products/add", headers=headerValues, data=body1)
    # context.put(url)
    print(response.status)
    result = response.json()
   
    print(result)

    assert response.status==201