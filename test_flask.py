import sys
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(request.args, file=sys.stderr)
    int_list = []
    for key in request.args:
        item = request.args[key]
        if item.isdigit():
            item = int(item)
            int_list.append(str(item**2))
    return ",".join(int_list)
    

	
if __name__ == "__main__": 
    app.run()

