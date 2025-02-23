from flask import Flask, jsonify, request
from flask_cors import CORS

# def read_file():
#     with open('./log.txt', 'r', encoding="utf-8") as file1:
#         data = file1.read()
#     print(data)
#     return data
#
# read_file()
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


data =[
    {
        'pc':'n1',
        'data_b': [
        {
            'time':"123",
            'data': "v r g r v ESCAPE"
        },
        {
            'time':"456",
            'data': "1 2 3   i z a k   k a k o n ESCAPE"
        },
        {
            'time':"789",
            'data': "i z a k   k a k o n   ALT_L SHIFT i z a j BACKSPACE k ESCAPE"
        }
    ]
},
    {
        'pc': 'n2',
        'data_b': [
            {
                'time': "9",
                'data': "v r g r v ESCAPE"
            },
            {
                'time': "3",
                'data': "1 2 3   i z a k   k a k o n ESCAPE"
            },
            {
                'time': "6",
                'data': "i z a k   k a k o n   ALT_L SHIFT i z a j BACKSPACE k ESCAPE"
            }
        ]
    }

    ]






# Get all students (name and ID only)
@app.route('/api/computers', methods=['GET'])
def get_computers():
    simplified_students = [{"pc": d["pc"]} for d in data]
    return jsonify(simplified_students)



# Get specific student details
@app.route('/api/computers/<pc>', methods=['GET'])
def get_pc(pc):
    my_pc = next((s for s in data if s['pc'] == pc), None)
    if my_pc:
        my_data = [{"time": d["time"], "data":d["data"]} for d in my_pc['data_b']]
        return jsonify(my_data)
    else:
        return jsonify({"error": "לא קיים מחשב זה"}), 404



# # Get all students (name and ID only)
# @app.route('/api/computers/data', methods=['GET'])
# def get_data():
#     simplified_students = [{"time": d["time"], "data": d["data"]} for d in data]
#     return jsonify(simplified_students)


if __name__ == '__main__':
    app.run(debug=True)




