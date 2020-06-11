import requests
from flask import Flask, request
import json

app = Flask(__name__)


# 只接受get方法访问
@app.route("/douyin/user", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    uid = get_data.get('uid')
    # 对参数进行操作
    return_dict['result'] = tt(uid)
    return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def tt(uid):
    try:
        url = 'https://api-service.chanmama.com/v1/home/author/info?author_id={}'
        res = requests.get(url.format(uid))
        return res.text
    except:
        return "请求失败"


if __name__ == "__main__":
    app.run(debug=True)
