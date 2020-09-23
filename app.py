# -*- coding:utf-8 -*-
import time

from io import BytesIO

try:
    import urllib2
except ImportError:
    import urllib.parse as urllib2
import xlrd
from flask import Flask, render_template, request
from flask import Response
from flask import make_response
from xlsxwriter.workbook import Workbook

from models import User

app = Flask(__name__)


def export_excel(filename, office):
    out_put = office.getvalue()
    output = make_response(out_put)
    output.headers[
        "Content-Disposition"] = "attachment; filename*=UTF-8''{0}.xlsx".format(
        urllib2.quote(filename.encode('utf-8')))
    output.headers[
        "Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    return output


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files['file']
    # print(f)
    # filename = f.filename
    # f.save(filename)
    # old_excel = xlrd.open_workbook(filename, encoding_override="utf-8")

    # buffer = io.BytesIO()
    # """文件save到buffer IO流中读写，效果等同于以上注释的代码"""
    # """xrd api:https://xlrd.readthedocs.io/en/latest/api.html"""
    # f.save(buffer)
    # buffer.seek(0)
    # old_excel = xlrd.open_workbook(file_contents=buffer.getvalue())
    """后来发现文件并不需要放入到io流中，file对象本身就是cpython实现的io流"""
    old_excel = xlrd.open_workbook(file_contents=f.read())

    sh = old_excel.sheets()[0]
    row_date = sh.row_values(0)
    print(row_date)
    lis = [u"序号", u"姓名", u"手机号码"]
    # if lis == row_date:
    for i in range(1, int(sh.nrows)):
        k = 0
        u = User()
        print(sh.row_values(0)[k], type(sh.row_values(i)[k]))
        u.username = sh.row_values(i)[k]
        u.pwd = sh.row_values(i)[k + 1]
        u.save()

    return render_template("index.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    filename = "123"
    output = BytesIO()
    office = Workbook(output)

    worksheet = office.add_worksheet()
    lis = [u"序号", u"姓名", u"手机号码"]
    bold = office.add_format({'bold': True})
    worksheet.write_row("A1", lis, bold)
    users = [type("A", (object,), {"username": 1123, "pwd":123})]
    i = 2

    for u in users:
        array = []
        array.append(str(i - 1))
        array.append(u.username)
        array.append(u.pwd)
        worksheet.write_row("A" + str(i), array, bold)
        i += 1
    office.close()
    return export_excel(filename, output)


@app.route('/large.csv')
def generate_large_csv():
    # 异步下载csv 文件, 问题:前端取消下载会触发socket error
    def generate():
        for row in range(200):
            line = []
            for col in range(50):
                line.append(str(col))

            if row % 1000 == 0:
                time.sleep(1)
                print('row: %d' % row)
            yield '\t'.join(line) + '\n'

    return Response(generate(), mimetype='text/csv')


if __name__ == "__main__":
    # pass
    app.run(port=5009, debug=True)
