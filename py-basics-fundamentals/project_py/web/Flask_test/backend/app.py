from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

message_list = []

@app.route("/")
def home():
    # Fixed: Changed variable name to 'messages' to match the HTML loop
    return render_template("index.html", messages=message_list)

# Fixed: Changed "Post" to all-caps "POST"
@app.route("/submit", methods = ["POST"])
def submit():
    user_text = request.form.get("feedback")
    if user_text:
        message_list.append(user_text)
    return redirect(url_for("home"))

@app.route("/delete", methods=["POST"])
def delete():
    target_message = request.form.get("message_to_delete")
    if target_message in message_list:
        message_list.remove(target_message)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
