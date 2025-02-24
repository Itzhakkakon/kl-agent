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


data_b =[
    {
        'pc':'n1',
        'time':"n123",
        'data': "v r g r v ESCAPE"
    },
    {
        'pc':'n2',
        'time':"n456",
        'data': "1 2 3   i z a k   k a k o n ESCAPE"
    },
    {
        'pc':'n1',
        'time':"n789",
        'data': "i z a k   k a k o n   ALT_L SHIFT i z a j BACKSPACE k ESCAPE"
    },
    {
        'pc': 'n2',
        'time': "n9",
        'data': "v r g r v ESCAPE"
    },
    {
        'pc': 'n1',
        'time': "3",
        'data': "1 2 3   i z a k   k a k o n ESCAPE"
    },
    {
        'pc': 'n2',
        'time': "n6",
        'data': "i z a k   k a k o n   ALT_L SHIFT i z a j BACKSPACE k ESCAPE"
    }
]






# Get all computers (all computers)
@app.route('/api/computers', methods=['GET'])
def get_computers():
    simplified_students = [d["pc"] for d in data_b]
    print(simplified_students)
    return jsonify(simplified_students)

def get_data(pc):
    return [d for d in data_b if d["pc"] == pc]


# Get specific pc details
@app.route('/api/computers/<pc>', methods=['GET'])
def get_pc(pc):
    pc_data = get_data(pc)
    print(pc_data)
    if pc_data:
        my_data = [{"time": d["time"], "data":d["data"]} for d in pc_data]
        return jsonify(my_data)
    return jsonify({"error": "לא קיים מחשב זה"}), 404


@app.route('/api/computers/<pc>/<time>', methods=['GET'])
def get_data_by_pc_with_time(pc, time):
    my_data = get_data(pc)
    if my_data:
        new_data = [{"data": d["data"]} for d in my_data if d["time"] == time]
        if new_data:
            return jsonify(new_data)
    return jsonify({"error": "לא קיים במחשב זה"}), 404


# Add new computers
@app.route('/api/computers', methods=['POST'])
def add_computers():
    new_computers = request.json

    # Check if computers with this PC already exists
    if any(s["pc"] == new_computers["pc"] for s in data_b):
        return jsonify({"error": "מחשב זה כבר קיים במערכת"}), 400

    # Add new computers
    data_b.append(new_computers)
    return jsonify(new_computers), 201


if __name__ == '__main__':
    app.run(debug=True)




