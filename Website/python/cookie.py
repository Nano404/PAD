from flask import request

if 'yummy_cookie' == 'admin' in request.cookies:
    return render_template('adminindex.html');
else:
    return render_template('index.html');