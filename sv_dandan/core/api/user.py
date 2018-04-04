# coding:utf-8
# @ Time :2018 /4/4
# @ File : api/user.py 
from api import api 
from flask import jsonify
tasks=[
        {
        }    
    ]

@api.route('/SignUp',methods=['POST'])
def d_register():
    if request.method == 'POST':
        phone=request.form.get('phone')
        pwd=request.form.get('PassWord')
        
    return jsonify(request.form)

@api.route('/txx')
def txx():
    return 'adf'
