from flask import Blueprint, request, jsonify, Response, current_app
from werkzeug.exceptions import Forbidden, Unauthorized
from auth_logic import check_auth, get_logged_in_user_id

bp = Blueprint("invoices", __name__)

default_page_size = 10

def generate_cache_invoices_page_key(page, size):
    return f'getInvoices-page{page}-size{size}'

@bp.get('/invoices/<int:page>')
def get_invoices_by_user(page):
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1, 2], ioc_container)

        if status == 0:
            page_key = generate_cache_invoices_page_key(page, default_page_size)
            if ioc_container.cache_manager.check_key(page_key):
                    results = ioc_container.cache_manager.get_data(page_key)
                    return Response(results, mimetype="application/json")
            else:
                user_id = get_logged_in_user_id(token, ioc_container)
                results = ioc_container.invoice_repository.get_invoice_info_by_user(user_id)

            if results:
                return jsonify(results), 200
            else:
                return jsonify([]), 200
        elif status == 1:
            raise Unauthorized("Login required/ Incorrect token.")
        elif status == 2:
            raise Forbidden("Insufficient permissions.")
    except Forbidden as ex:
        return jsonify(message=str(ex)), 403
    except Unauthorized as ex:
        return jsonify(message=str(ex)), 401
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500