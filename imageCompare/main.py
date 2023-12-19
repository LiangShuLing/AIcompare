import os
import sys

from flask import (
    Flask, render_template, request, redirect, globals
)
# from werkzeug.utils import secure_filename

# import test1
import imageCompare3
# import clearResult
app = Flask(__name__)
sysPath = sys.path[0]
imgPath = os.path.join(sysPath,"originImages")
app.config['UPLOAD_FOLDER'] = imgPath
app.config['ALLOWED_EXTENSIONS'] = set(['png','jpg'])

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     clearResult.clear()
#     return render_template(
#         "b.html"
#     )
@app.route("/first", methods=['GET', 'POST'])
def first():
    return render_template(
        "first.html"
    )

@app.route("/first2", methods=['GET', 'POST'])
def first2():
    return render_template(
        "first2.html"
    )
@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = os.listdir(imgPath)
        for file in files:
            os.remove(os.path.join(imgPath,file))
        f1 = request.files['img1']
        f2 = request.files['img2']
        print(f1.filename)
        f1.save(imgPath+"/"+"image1."+f1.filename.split('.')[-1])
        f2.save(imgPath+"/"+"image2."+f2.filename.split('.')[-1])
        imageCompare3.compare_images('./originImages/image1.jpg', './originImages/image2.jpg',
            './static/img/diff.jpg','./static/img/result.jpg')
        return render_template(
            "b2.html"
        )
    else:
        return render_template("upload.html")



# @app.route("/test", methods=['GET', 'POST'])
# def test():
#     test1.run()
#     imageCompare3.compare_images('./originImages/image1.jpg','./originImages/image2.jpg',
#     './static/img/diff.jpg','./static/img/result.jpg')
#     return render_template("b2.html")

@app.route("/imagecompare", methods=['GET', 'POST'])
def imagecompare():
    imageCompare3.compare_images('./originImages/image1.jpg','./originImages/image2.jpg',
    './static/img/diff.jpg','./static/img/result.jpg')
    return "Successful"





if __name__ == '__main__':
    app.run(debug=True)