from flask_paginate import Pagination, get_page_parameter # 分页
from flask import request

def query_objects_pagination(query_objects, per_page):
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, per_page=per_page ,total=query_objects.count(), bs_version=4, search=search)
    pagination_items = query_objects.paginate(page=page, per_page=per_page).items
    return {'pagination':pagination, 'pagination_items': pagination_items}