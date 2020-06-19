import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
    
    var HttpRequestEntity = Java.use('com.cmbchina.ccd.library.cache.a.a');//要hook的类名完整路径

    HttpRequestEntity.getSign.implementation = function () { // 重写要hook的方法getSign，当有多个重名函数时需要重载，function括号为函数的参数个数
       
        var Sign=this.getSign(); //调用原始的函数实现并且获得返回值，如果不写的话我们下面的代码会全部替换原函数
       
        send(p1)
        send(Sign);   //打印返回值
        return Sign;  //函数有返回值时需要返回
    };
    
});
"""

process = frida.get_usb_device().attach('com.cmbchina.ccd.pluto.cmbActivity')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()