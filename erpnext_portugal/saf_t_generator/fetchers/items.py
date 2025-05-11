import frappe

def get_items():
    items = frappe.get_all("Item", filters={"disabled": 0}, fields=[
        "item_code", "item_name", "item_group", "is_stock_item"
    ])
    return [{
        "ProductType": "P" if item.is_stock_item else "S",
        "ProductCode": item.item_code,
        "ProductDescription": item.item_name,
        "ProductNumberCode": item.item_group
    } for item in items]