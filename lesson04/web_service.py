from flask import Flask, request, make_response, jsonify
import json

app = Flask(__name__)


def load_grade():
    grade_list = dict()
    with open("./grade.csv", "r") as file:
        for record in file.readlines():
            record = record.replace("\n", "")
            items = record.split(",")
            if str(items[0]) not in grade_list:
                grade_list[str(items[0])] = list()
            grade_list[str(items[0])].append({str(items[1]): str(items[2])})
    return grade_list


@app.route('/', methods=['POST'])
def check_grade():
    req = request.get_json(silent=True, force=True)
    try:
        query_result = req.get("queryResult")
    except AttributeError:
        return 'JSON error'

    # Action Switcher
    print("queryResult = {}".format(req.get("queryResult")))
    return_message = "ไม่พบข้อมูล"
    if query_result.get("action") == "check-grade":
        id = "{0:.0f}".format(query_result.get("parameters").get("id"))
        code = str(query_result.get("parameters").get("code"))
        grade_list = load_grade()
        print("grade_list: {}".format(json.dumps(grade_list)))
        if id in grade_list:
            for subject in grade_list[id]:
                if code in subject:
                    grade = subject[code]
                    return_message = "เกรดรายวิชา {} ของนักศึกษารหัส {} ได้เกรด {}".format(code, id, grade)

    return make_response(jsonify({"fulfillmentText": return_message}))


if __name__ == "__main__":
    app.run(debug=True, port=80)
