import uiautomator2 as u2

d = u2.connect('127.0.0.1:21503') # 连接设备







d(text="微信").click()
d(resourceId="com.tencent.mm:id/edu").click()
d(resourceId="com.tencent.mm:id/li").click()
d.set_fastinput_ime(True)
d.send_keys("18215621840")
d.set_fastinput_ime(False)
d(resourceId="com.tencent.mm:id/b0f").click()
d(resourceId="com.tencent.mm:id/cvf").click()
d(resourceId="com.tencent.mm:id/de0").click()
d(resourceId="com.tencent.mm:id/b29").click()
d(resourceId="com.tencent.mm:id/li", text="请填写验证码").click()
verification = input("输入验证码:")
d.set_fastinput_ime(True)
d.send_keys(verification)
d.set_fastinput_ime(False)
d(resourceId="com.tencent.mm:id/b0f").click()


# d(resourceId="com.tencent.mm:id/b0f").click()


# d(text="饿了么").click()
# d(scrollable=True).scroll(steps=10)
# # d(scrollable=True).scroll.vert.backward()
# d(resourceId="me.ele:id/check_shops_near_by").click()
# d(resourceId="me.ele:id/buttonDefaultPositive").click()
# d(resourceId="me.ele:id/mobile_number").click()
# d.set_fastinput_ime(True)
# d.send_keys("18215621840")
# d.set_fastinput_ime(False)
# d(resourceId="me.ele:id/send_sms_verification_code").click()






# d.xpath('//*[@resource-id="me.ele:id/verification_code"]/android.widget.LinearLayout[1]').click()

# d.click(0.336, 0.679)
# d.xpath('//*[@text="饿了么"]').click()
# d(scrollable=True).scroll(steps=10)
# d.click(0.516, 0.398)
# d(scrollable=True).scroll(steps=10)


# d(scrollable=True).scroll.vert.backward()
# d(text="微信").click()