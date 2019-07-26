from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

orders = []
order_no = 1

@app.route('/')
def home():
    return 'This is Home!'

@app.route('/mypage')
def mypage():
    return render_template('index.html')

@app.route('/ordertable')
def order():
    return render_template('ordertable.html')


@app.route('/post', methods=['POST'])
def post():
    global orders
    global order_no

    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    order = {'no': order_no, 'name': name_receive , 'number': number_receive, 'address': address_receive, 'phone': phone_receive}

    order_no = order_no + 1

    orders.append(order)


    return jsonify({'result': 'success'})


@app.route('/post', methods=['GET'])
def view():
    return jsonify({'result': 'success', 'orders': orders})



if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)