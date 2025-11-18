from flask import Blueprint, request, jsonify, Response, current_app
from werkzeug.exceptions import Forbidden, Unauthorized
from auth_logic import check_auth, get_logged_in_user_id

bp = Blueprint("payments", __name__)

@bp.post('/paymentmethods')
def register_payment_method():
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:            
            if not request.is_json:
                    return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            if "brand" not in body:
                raise ValueError("error: Brand required.")
            if "last4" not in body:
                raise ValueError("error: Last 4 digits required.")
            if "exp_month" not in body:
                raise ValueError("error: Expiring month required.")
            if "exp_year" not in body:
                raise ValueError("error: Expiring year required.")
            
            user_id = get_logged_in_user_id(token, ioc_container)
            ioc_container.payment_method_repository.insert_payment_method(user_id, body.get('brand'), body.get('last4'), body.get('exp_month'), body.get('exp_year'))
            return jsonify({"message": "Payment method inserted successfully!"}), 200
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


@bp.get('/paymentmethods')
def get_payment_methods():
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            user_id = get_logged_in_user_id(token, ioc_container)           
            results = ioc_container.payment_method_repository.get_payment_methods_by_user_id(user_id)
            return jsonify(results), 200
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



@bp.put('/paymentmethods/<int:pm_id>')
def update_payment_method(pm_id):
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0: 
            if not request.is_json:
                    return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}
        
            if "user_id" not in body:
                raise ValueError("error: User ID required.")
            if "brand" not in body:
                raise ValueError("error: Brand required.")
            if "last4" not in body:
                raise ValueError("error: Last 4 digits required.")
            if "exp_month" not in body:
                raise ValueError("error: Expiring month required.")
            if "exp_year" not in body:
                raise ValueError("error: Expiring year required.")
            
            ioc_container.payment_method_repository.update_payment_methods_by_id(pm_id, body.get('user_id'), body.get('brand'), body.get('last4'), body.get('exp_month'), body.get('exp_year'))

            return jsonify({"message": "Product updated successfully!"}), 200
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


@bp.delete('/paymentmethods/<int:pm_id>')
def delete_payment_method(pm_id):
    ioc_container = current_app.ioc
    try:
        token = request.headers.get('Authorization')
        status = check_auth(token, [1], ioc_container)

        if status == 0:       
            ioc_container.payment_method_repository.delete_payment_methods_by_id(pm_id)
            return jsonify({"message": "Product deleted successfully!"}), 200
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
        