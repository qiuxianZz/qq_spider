import requests


url = 'https://aweme.snssdk.com/aweme/v1/user/?sec_user_id=MS4wLjABAAAAiLZ5KIxr6MUR4E0nPIU9GMupnsup6jqBWWkFSeltoF0&address_book_access=2&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=970&dpi=192&uuid=861143247784164&app_name=douyin_lite&version_name=9.7.0&ts=1587373313&app_type=normal&ac=wifi&update_version_code=9702&channel=360_lite_aweme&_rticket=1587372144906&device_platform=android&iid=113035172582&version_code=970&cdid=f98c5820-3a43-41d5-bb75-ef426599cdc6&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=2329&mcc_mnc=46000'
url = 'https://aweme.snssdk.com/aweme/v1/user/?sec_user_id=MS4wLjABAAAABvwOLdm1R6t-IZujPh9PFDRq1ZGxQ027jsZIqyCRuNE&address_book_access=2&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=970&dpi=192&uuid=861143247784164&app_name=douyin_lite&version_name=9.7.0&ts=1587373860&app_type=normal&ac=wifi&update_version_code=9702&channel=360_lite_aweme&_rticket=1587372690533&device_platform=android&iid=113035172582&version_code=970&cdid=f98c5820-3a43-41d5-bb75-ef426599cdc6&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=2329&mcc_mnc=46000'
# url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&max_cursor=0&sec_user_id=MS4wLjABAAAAKs3kbXxA-YrO4KeKCbDX7_NhM-B4QI19HMskzuAa_hg_PXTXwzelIGGaomyS_rff&count=20&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=970&dpi=192&uuid=861143247784164&app_name=douyin_lite&version_name=9.7.0&ts=1587373745&app_type=normal&ac=wifi&update_version_code=9702&channel=360_lite_aweme&_rticket=1587372576114&device_platform=android&iid=113035172582&version_code=970&cdid=f98c5820-3a43-41d5-bb75-ef426599cdc6&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=2329&mcc_mnc=46000'
# url = 'https://aweme.snssdk.com/aweme/v1/user/?user_id=88445518961&address_book_access=1'
# url = 'https://aweme-eagle.snssdk.com/aweme/v1/user/?sec_user_id=MS4wLjABAAAAN3xKYzz9F1yOUXgqtORq5lmwFuaxSSYJyi7_kX1AuW0&user_id=95192769636&address_book_access=1&retry_type=no_retry'
header = {
    # "Accept-Encoding": "gzip",
    # "X-SS-REQ-TICKET": "1587372144895",
    # "sdk-version": "1",
    "User-Agent": "ttnet okhttp/3.10.0.2",
    # "Cookie": "install_id=113035172582; ttreq=1$50b18a06fc53b92e6990e692c74d1ac63f0f8935; odin_tt=4cf050e3ee42b51d503006da985cdecb82f62de3a7a2170a8e9e0fdd7cf0a4aa5d5a8ac201933642d1e54148f613e4e26f7ee8d97e108d8f66a097cbc48fe387; passport_csrf_token=1f94a64ed2840d70b676550f6a6ea664",
    # "X-Gorgon": "040100e640052121f7db27bbe3174e2c8d729c20afc906b96b3a",
    # "X-Khronos": "1587372144",
    # "Host": "aweme.snssdk.com",
    # "Connection": "Keep-Alive"


}



url = 'https://api-service.chanmama.com/v1/home/author/info?author_id=2365744590893533'
res = requests.get(url,headers=header)
print(res.text)
