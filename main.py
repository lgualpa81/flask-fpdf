import json, asyncio
from flask import Flask, request, jsonify
from jobs.tasks import do_other_things
from fpdf import FPDF
import base64

app = Flask(__name__)

async def main_tasks():
    await asyncio.gather(do_other_things(5), do_other_things(2)) # non block here
    #await asyncio.create_task(do_other_things(5))
    #await task1


@app.route('/',methods = ['GET','POST'])
def index():
    asyncio.run(main_tasks())

    return jsonify({"hello":"world"})

@app.route("/pdf", methods=["GET"])
def pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    # pdf.output('example1.pdf', 'F')
    pdf_file = pdf.output(dest='S')
    encoded_string = base64.b64encode(pdf_file).decode()

    return jsonify({"pdf_b64":encoded_string})

app.run(debug=True)
