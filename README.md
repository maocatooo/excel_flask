# excel_flask
flask_excel 的上传下载

f = request.files['file']
buffer = io.BytesIO()
"""文件save到buffer IO流中读写，效果等同于以上注释的代码"""
"""xlrd api:https://xlrd.readthedocs.io/en/latest/api.html"""
f.save(buffer)
buffer.seek(0)
old_excel = xlrd.open_workbook(file_contents=buffer.getvalue())
