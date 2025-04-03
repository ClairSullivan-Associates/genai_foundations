from flask import Flask, request, jsonify
import jinja2

app = Flask(__name__)
app.config["DEBUG"] = True

def x(r):
    e = jinja2.Environment()
    t = e.from_string("from flask import Flask, request, jsonify\napp = Flask(__name__)\n@app.route('/{{a}}', methods=['POST'])\ndef h():\n d = request.get_json()\n if not d:\n  return jsonify({'error':'No data provided'}), 400\n return jsonify({'result': d}), 200\nif __name__=='__main__':\n app.run()")
    return t.render(a=r)

def y():
    z = ["credit", "debit", "refund", "authorize", "chargeback"]
    m = {}
    for i in z:
        n = x(i)
        m[i] = n
    return m

@app.route("/generate", methods=["GET"])
def g():
    return jsonify(y())

if __name__ == "__main__":
    app.run(port=5000)
