# -*- coding:utf-8 -*-
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import json

res = """[{"res":"success","data":[{"JZGL":"25345.29","YMLSTR":[{"value":122741,"name":"浙能","itemStyle":[{"color":"#5470c6"}]},{"value":65567.3984375,"name":"国能","itemStyle":[{"color":"#fac858"}]},{"value":26206.279296875,"name":"华能","itemStyle":[{"color":"#ee6666"}]},{"value":15638.9404296875,"name":"大唐","itemStyle":[{"color":"#73c0de"}]},{"value":0,"name":"华电","itemStyle":[{"color":"#3ba272"}]},{"value":8999.0595703125,"name":"华润","itemStyle":[{"color":"#fc8452"}]},{"value":0,"name":"台塑","itemStyle":[{"color":"#9a60b4"}]},{"value":0,"name":"巨化","itemStyle":[{"color":"#ea7ccc"}]}],"STATSTR":[{"cydl1":"4.95","cydl2":"3.62","jtmc":"浙能","mh1":"241.08","mh2":"216.92","name":"","qjrhl1":"6213.82","qjrhl2":"5582.64","value":"91.33"},{"cydl1":"4.42","cydl2":"4.05","jtmc":"国能","mh1":"289.19","mh2":"242.80","name":"","qjrhl1":"7623.76","qjrhl2":"6109.44","value":"92.96"},{"cydl1":"3.47","cydl2":"3.47","jtmc":"华能","mh1":"241.26","mh2":"236.85","name":"","qjrhl1":"6328.75","qjrhl2":"6296.34","value":"92.25"},{"cydl1":"5.65","cydl2":"4.04","jtmc":"大唐","mh1":"324.60","mh2":"230.07","name":"","qjrhl1":"8194.65","qjrhl2":"5892.66","value":"92.24"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"华电","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"},{"cydl1":"1.97","cydl2":"4.06","jtmc":"华润","mh1":"288.55","mh2":"286.66","name":"","qjrhl1":"7523.78","qjrhl2":"7534.98","value":"92.65"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"台塑","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"巨化","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"}],"SSFH":"24664.55","LJFD":"609441.06"}]}]"""

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
