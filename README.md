This is my project which is used to as a **graduation design**.
So, Please not using it to as your graduation design and conflict with me in 2019.

Notes: 

If you want to use this system, you should change some code in flask_login/utils.py.
 There is a function called by login_required, we should rewrite it.
 
 Add a function :
 
     def login_error_handle():
        data = json.dumps({
            "code": 1,
            "msg": "请先登录",
            "result": ""
        })
        return Response(data, mimetype="application/json;charset=utf-8")
    
And you also notes in function "decorated_view"

     return current_app.login_manager.unauthorized()