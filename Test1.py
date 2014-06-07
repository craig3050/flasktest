from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<number>")
def hello(number):

    templateData = {
      'title' : "All the numbers up to...",
      'numbers' : give_number(number)
    }

    return render_template('Test1.html', **templateData)

def give_number(number):
    start = 1
    numbers = []
    while start != int(number):
        numbers.append(start)
        start += 1
    print numbers
    final = "= "
    for item in numbers:
        final = final + str(item) + ", "
        print final
    return final

if __name__ == "__main__":
    app.run(host='192.168.0.3', port=80, debug=True)
