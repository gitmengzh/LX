#coding:utf-8
#@time     :     2018/11/26 18:41
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : post.py
# @Software: PyCharm

'''
import requests, json



headers={'Content-Type': 'application/x-www-form-urlencoded'}


url = "http://172.0.2.143/login"

postdata = {
"username": "admin@securebox.comodo.com",
"password": "secret1"
}

response = requests.post(url,data=json.dumps(postdata), headers=headers)

print (response.text)'''


import requests
import json

# 头部信息
url = "http://172.0.2.143/rest/app_policies/generate"
headers = {
    "Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
"Connection": "keep-alive",
"Content-Length": "3758",
"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLmBCbAItaLJroxi5",
"Cookie": "COOKIE_LOCALE_LANG=%22en-US%22; JSESSIONID=730EE4D16D554531947CAD2A2C86B9C3",
"Host": "172.0.2.143",
"Origin": "http://172.0.2.143",
"Referer": "http://172.0.2.143/",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
postdata={
#'data':'test'
'data': {"id":"null","appType":0,"policyId":"5bfbc61450630334e5474026","iconFileId":"null","iconFileName":"null","logoFileId":"null","logoFileName":"null","adminPassword":"null","userPassword":"null","openPassword":"null","sha1":"null","secureFileId":"null","secureFileName":"null","path":"www.qq.com","directory":"null","genkeyVersion":"null","fromCMCServer":1,"management":{"standalone":0,"managementServer":"http://172.0.2.143","logServer":"null","upgradeServer":"","licensePath":"null","installerPath":"null","trustedCertificateList":"null","flsUri":"null","camUri":"null","upgradeUsingComodoServerFirst":0,"dragonPath":"null","logFormat":1},"settings":{"version":"1","timeServer":"","userId":"null","preventOfflineAccess":0,"forceUpgrade":0,"upgradeLicense":0,"scanInBackground":1,"scanOption":2,"autoInstall":1,"fullScreen":0,"downloadPrevention":0,"privateMode":1,"useDefaultDataFolder":0,"singleProcessMode":1,"noFrameMerging":1,"singleInstanceMode":1,"blockPrtScnKey":1,"autoClosed":1,"integrityCheck":0,"appFilterBehavior":2,"outsideLaunchFilterBehavior":2,"closeRunningApps":0,"preventAppMin":0,"saveProtection":0,"autoStart":0,"showSwitchBtn":1,"showKeyboardBtn":1,"protectHostsFile":1,"lockTime":0,"secureRDPList":[],"alwaysOpenInCSB":0,"lockTaskbar":1,"showSettingDialog":0,"showInstantMsg":0,"showPostMessage":0,"email":"secureboxsupport@comodo.com","showCollectSystemInformation":0,"showMyApps":0,"showMyFavorWeb":0,"myFavorWebList":[],"secureCertificate":2,"ieTrust":0,"activex":2,"pop_up":2,"ieTrustList":[],"addonAndExtension":0,"addonAndExtensionList":[]},"protectData":{"setUserPwd":0,"forceRestartSystem":0,"editPwd":"false","needGetOld":"false","pathList":[]},"restrictedFolder":{"pathList":[]},"appPath":{"appPathList":[]},"filtering":{"enabledAllowedApp":-1,"allowedAppList":[],"allowedServiceList":[],"enabledDeviceBlocked":0,"setBlockedIP":0,"setDnsConfigration":0,"dnsConfigrationList":[],"enableOutsideLaunchAppFilter":0,"outsideLaunchAppFilterList":[],"vendorList":["Microsoft Corporation","IEBLD Builder Account","Code Systems Corporation","Google Inc","Mozilla Corporation","Comodo Security Solutions, Inc.","Comodo Security Solutions, Inc","Comodo Security Solutions","Microsoft Windows","Microsoft Windows Component Publisher"],"enableOutsideProtect":0,"blockedIpRangeList":[],"enableAllowedUrl":0,"allowedUrlList":[],"deviceFilterList":[],"enableWebsiteRedirect":0,"websiteRedirect":[]},"secureApps":{"productName":"test4","category":"null","useCam":0,"camGuid":"F501E2D6-9C4B-4AD1-9030-A49E370B1A8C","identifier":"null","rootCertCheck":1,"antiInjection":1,"keyboardProtection":1,"processScan":1,"remoteCheck":1,"desktopIsolation":1,"copyPasteProtection":1,"setOpenPassword":0,"enablePasswordsProtect":0,"lockPasswordTime":30,"lockPasswordCount":5,"folderModeBlockProcess":1,"remoteExcludeList":[],"bomgarIpRange":[],"teamViewerIpRange":[],"logmeinIpRange":[],"goToMeetingIpRange":[],"defaultBrowserIE":1,"defaultBrowserIECheckSignature":1,"defaultBrowserIECheckVendor":1,"defaultBrowserIESha1":"","portableIePath":"null","enablePrivateRootCert":0,"privateRootCertValue":0,"privateRootCertPath":"","encryptionKey":"CCE17D25EEF146D2","verifyModeVendor":0,"verifyModeSha1":0,"vendor":"null","sha1":"null","featureCertification":0,"certificateVerification":0,"certKey":[],"installCertKey":[],"installCerPath":"null","folderModeSignature":0,"folderModeVendor":0,"folderModeSha1":"","folderModeExtension":[],"secureAppType":"Default","folderEnableCopyFileToSE":0,"folderCopyFileToSE":[],"folderEnableCopyFileFromSE":0,"folderCopyFileFromSE":[]},"vpn":{"natServer":"null","relayServer":"null","server":"null","virtualHubName":"null","port":"443"},"appPolicyName":"null"}

}
response = requests.post(url,data=json.dumps(postdata), headers=headers)

print (response.text)


