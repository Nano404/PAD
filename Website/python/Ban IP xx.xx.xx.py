from flask import request, abort, current_app as app

ip_ban_list = ['127.0.0.1']


def block_method():
    ip = request.environ.get('REMOTE_ADDR')
    if ip in ip_ban_list:
        abort(403)