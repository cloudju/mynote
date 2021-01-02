1. 取得一个url
1. 判断url in masterDict
2. 下载url内容到变量html
2. 计算url的sha256
2. 用sha256作为文件名保存html内容。
3. 用butifulsoup取得html中所有url保存为links数组
3. 将url，文件路径，保存为一个dic。
4. masterDict[sha256]=dic
5. for url in links
1. goto 1
