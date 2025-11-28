
def complete_sale(sales_date, total_amount, user_id, lines, ioc_container):
    try:
        for line in lines:
            product_id = line.get('product_id')
            exists_product = ioc_container.product_repository.get_products_by_id(product_id)
            stock_qty = exists_product.get('stock_qty')
            qty = line.get('quantity')
            

            #Checking if the product exists first
            if not exists_product:
                raise ValueError(f"Product does not exist (Product id: {product_id})")
            #If it exists then need to check if there is enough stock or if there is stock at all
            elif(stock_qty <= 0 or qty > stock_qty):
                raise ValueError(f"Not enough stock for Product id: {product_id})")
            else:
                #If it exists I need to add to the lines dictionary the values unit_price and subtotal
                unit_price = exists_product.get('unit_price')
                line['unit_price'] = unit_price
                line['subtotal'] = unit_price * line.get('quantity')

        #If it passes the previous validations (Product and stock exists), then first we create the invoice header
        #This inserts the new invoice and returns the ID which I store in invoice_id for later use
        invoice_id = ioc_container.invoice_repository.insert_invoice_headers(sales_date, total_amount, user_id)
        #I then need to add the invoice id to each dict in the lines list for creating the invoice lines with the correct invoice id/
        #I also need to add the subtotal as 0 for each linme
        for line in lines:
            line['invoice_id'] = invoice_id
        #This is to see what the lines list prints before inserting them in the invoice lines table
        print(lines)
        #Then we create the lines for the products user will buy
        ioc_container.invoice_repository.insert_invoice_lines(lines)
        #Then we get the total amount for the new sale
        total = ioc_container.invoice_repository.get_total_invoice_by_id(invoice_id)
        #We update the invoice header to have the correct total amount
        ioc_container.invoice_repository.update_total_amount_invoice_headers(total, invoice_id)
        #Now we go and reduce the stock for the iterms boought
        for line in lines:
            quantity = line.get('quantity')
            product_id = line.get('product_id')

            ioc_container.product_repository.reduce_stock_product(product_id, quantity)
    except ValueError as ex:
        raise ValueError(ex)
    except Exception as ex:
        raise Exception(ex)