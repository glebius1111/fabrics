import os
import subprocess

from flask import Flask, render_template, request, jsonify
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import index

# create flask instance
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024

indexer = index.Index()



INDEX_PATH = os.path.join(os.path.dirname(__file__), 'index.pickle')

MAX_FILE_SIZE = 1024 * 1024 * 32

loaded_image = None

# main route
searcher = Searcher(INDEX_PATH)
    #return render_template("index.html", args=args)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    indexer.reindex()
    searcher.read()
    return render_template('index.html', forward_message=forward_message);

@app.route('/search', methods=['POST'])
def search():
    print('dsds')
    if request.method == "POST":

        RESULTS_ARRAY = []

        # get url
        image_url = request.form.get('img')

        try:

            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))

            # load the query image and describe it
            from skimage import io

            print(image_url)
            query = io.imread(image_url)
            features = cd.describe(query)
            # perform the search

            results = searcher.search(features)

            # loop over the results, displaying the score and image name

            for (score, resultID) in results:
                print(resultID)
                RESULTS_ARRAY.append(
                    {"image": str(resultID), "score": str(score)})

            # return success
            return jsonify(results=(RESULTS_ARRAY))

        except:

            # return error
            jsonify({"sorry": "Sorry, no results! Please try again."}), 500

@app.route("/load", methods=["POST", "GET"])
def load_file():
    print('dsf')
    RESULTS_ARRAY = []

    args = {"method": "GET"}
    if request.method == "POST":
        loaded_image = request.files["file"]
        loaded_image.save(loaded_image.filename)
        try:

            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))

            # load the query image and describe it
            from skimage import io

            query = io.imread(loaded_image.filename)
            features = cd.describe(query)
            # perform the search

            results = searcher.search(features)            # loop over the results, displaying the score and image name
            string = ''
            for (score, resultID) in results:
                print(resultID)
                s = ('< img src ="africa_fabric/'+str(resultID)+'"class ="result-img" > score ='+str(score)+'<br>')
                string += s
            # return success


        except:

            # return error
            jsonify({"sorry": "Sorry, no results! Please try again."}), 500
        print(string)
        return string


# run!
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
