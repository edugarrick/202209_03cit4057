# Enter your code here
from flask import Flask, jsonify
import os
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"
@app.route('/api/v1/teachingplan', methods=['GET'])
def get_books():
    return jsonify({"teachingplan":teachingplan})
@app.route('/api/v1/teachingplan/<int:id>', methods=['GET'])
def get_book(id):
    ch = [ch for ch in teachingplan if ch['id'] == id]
    return jsonify({'ch': ch})
teachingplan = [
 {
"id":0,
"title":"Course overview and Introduction",
 },
 {
"id":1,
"title":"Basic Elements",
 },
 {
"id":2,
"title":"Data Types",
 },
 {
"id":3,
"title":"Development Tools",
 },
 {
"id":4,
"title":"Control flow (1)",
 }
 ]
if __name__ == "__main__":
    os.chdir(".\\lab04\\22563705\\")
    app.run(debug=True)