# -*- coding:utf-8 -*-
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import json

res = """[{"res":"success","data":[{"JZGL":"23253.47","YMLSTR":[{"value":"57.10","name":"浙能","itemStyle":[{"color":"#9297F5"}]},{"value":"23.48","name":"国能","itemStyle":[{"color":"#5CDB92"}]},{"value":"10.33","name":"华能","itemStyle":[{"color":"#E0EC84"}]},{"value":"6.63","name":"大唐","itemStyle":[{"color":"#5A69E7"}]},{"value":"0","name":"华电","itemStyle":[{"color":"#E4986C"}]},{"value":"2.46","name":"华润","itemStyle":[{"color":"#C973DF"}]},{"value":"0","name":"台塑","itemStyle":[{"color":"#38D3A0"}]},{"value":"0","name":"巨化","itemStyle":[{"color":"#95EFFF"}]}],"STATSTR":[{"cydl1":"3.39","cydl2":"3.95","jtmc":"浙能","mh1":"231.20","mh2":"240.93","name":"","qjrhl1":"5949.97","qjrhl2":"6168.92","value":"93.06"},{"cydl1":"4.42","cydl2":"4.03","jtmc":"国能","mh1":"250.21","mh2":"239.80","name":"","qjrhl1":"6302.48","qjrhl2":"6067.00","value":"92.93"},{"cydl1":"3.47","cydl2":"3.47","jtmc":"华能","mh1":"190.25","mh2":"236.14","name":"","qjrhl1":"5000.57","qjrhl2":"6275.77","value":"92.96"},{"cydl1":"4.26","cydl2":"0.00","jtmc":"大唐","mh1":"236.82","mh2":"228.11","name":"","qjrhl1":"6026.04","qjrhl2":"5845.15","value":"92.49"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"华电","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"},{"cydl1":"1.93","cydl2":"3.81","jtmc":"华润","mh1":"282.67","mh2":"0.00","name":"","qjrhl1":"7443.46","qjrhl2":"7438.50","value":"91.84"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"台塑","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"巨化","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"}],"SSFH":"25834.28","LJFD":"553300.7"}]}]"""

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081", "http://127.0.0.1:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/jndpportal/wbjk/getSJGL.xhtml")
async def home():
    return json.loads(res)


if __name__ == "__main__":
    uvicorn.run("demo:app", host="localhost", port=8080, reload=True)
