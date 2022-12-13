from flask import Flask, request, jsonify
import werkzeug
import pytesseract
import easyocr
import cv2

app = Flask(__name__)


@app.route('/upload',methods=["POST"])
def upload():
    if(request.method == "POST"):
        imagefile = request.files['image']
        #### this code so that there is no need to save the image in memory
        # read image file string data
        # filestr = imagefile.read()
        # # convert string data to numpy array
        # file_bytes = numpy.fromstring(filestr, numpy.uint8)
        # # convert numpy array to image
        # img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

        #### this code to save img in memory
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        image_path = "./uploadedimages/" + filename
        imagefile.save(image_path)
        ## this is the code to process image to find result
        reader = easyocr.Reader(['vi', 'en'])  # this needs to run only once to load the model into memory
        result = reader.readtext(image_path,detail = 0,paragraph= True)
        print(result)
        data=""
        for i in result:
            data = data + "\n" + i;
        print(data)
        return jsonify(data)


@app.route('/test',methods=["GET"])
def test():
    return jsonify({
     "massage": "API OK"
    })


if __name__ == "__main__":
    app.run()

