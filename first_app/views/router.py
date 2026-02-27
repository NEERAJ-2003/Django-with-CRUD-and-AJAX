from .employee import *
from .auth import *


def load_page(request, page):

    if page == "list":
        return employee_list(request)

    if page == "create":
        return employee_create(request)

    if page.startswith("edit-"):
        emp_id = int(page.split("-")[-1])
        return employee_update(request, emp_id)

    if page.startswith("delete-"):
        emp_id = int(page.split("-")[-1])
        return employee_delete(request, emp_id)

    if page.startswith("detail-"):
        emp_id = int(page.split("-")[-1])
        return employee_detail(request, emp_id)

    if page == "login":
        return login_view(request)

    if page == "signup":
        return signup_view(request)

    if page == "forgot":
        return forgot_view(request)

    if page == "logout":
        return logout_view(request)

    return login_view(request)