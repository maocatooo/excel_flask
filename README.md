# excel_flask
flask_excel 的上传下载

f = request.files['file']

buffer = io.BytesIO()

"""文件save到buffer IO流中读写"""

"""xlrd api:https://xlrd.readthedocs.io/en/latest/api.html"""
```
f.save(buffer)

buffer.seek(0)

old_excel = xlrd.open_workbook(file_contents=buffer.getvalue())
```

"""后来发现文件并不需要放入到io流中，file对象本身就是cpython实现的io流"""

```
old_excel = xlrd.open_workbook(file_contents=f.read())
```