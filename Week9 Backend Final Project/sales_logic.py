# sales_logic.py

def complete_sale(sales_date, invoice_address, payment_method, user_id, shopping_cart_info, ioc_container):
    try:
        total_amount = 0
        for item in shopping_cart_info:
            product_id = item.get('product_id')
            exists_product = ioc_container.product_repository.get_products_by_id(product_id)

            # 1) Check existence first
            if not exists_product:
                raise ValueError(f"Product does not exist (Product id: {product_id})")

            # 2) Now it's safe to read fields
            stock_qty = exists_product.get('stock_qty')
            qty = int(item.get('quantity', 0))

            # 3) Stock validation
            if stock_qty <= 0 or qty > stock_qty:
                raise ValueError(f"Not enough stock for Product id: {product_id})")

            # 4) Compute subtotal and accumulate total
            item['subtotal'] = float(item['unit_price']) * qty
            total_amount += item['subtotal']

        # Payment method validation
        pm = ioc_container.payment_method_repository.get_payment_methods_by_user_id(payment_method)
        if pm is None:
            raise ValueError(f"Invalid payment method: {payment_method})")

        # Create header
        invoice_id = ioc_container.invoice_repository.insert_invoice_headers(
            sales_date, total_amount, invoice_address, payment_method, user_id
        )

        # Build lines
        lines = []
        for item in shopping_cart_info:
            lines.append({
                'quantity': int(item['quantity']),
                'unit_price': float(item['unit_price']),
                'subtotal': float(item['subtotal']),
                'product_id': item['product_id'],
                'invoice_id': invoice_id
            })

        # Insert lines
        ioc_container.invoice_repository.insert_invoice_lines(lines)

        # Decrease stock
        for line in lines:
            ioc_container.product_repository.modify_stock_product(
                0, line['product_id'], int(line['quantity'])
            )

        # Empty cart
        ioc_container.cart_repository.delete_cart_by_user_id(user_id)

    except ValueError as ex:
        # Preserve ValueError for tests / caller
        raise
    except Exception as ex:
        # Optional: let unexpected errors bubble unchanged, or wrap with context
        raise
