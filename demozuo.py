# -*- coding:utf-8 -*-
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import json

res = """[{"res":"success","data":[{"JZGL":"22491.94","FHSTR":[{"value":"49.98","name":"浙能"},{"value":"21.94","name":"国能"},{"value":"15.88","name":"华能"},{"value":"6.15","name":"大唐"},{"value":"0","name":"华电"},{"value":"5.65","name":"华润"},{"value":"0.40","name":"台塑"},{"value":"0","name":"巨化"}],"MJFH":"23765.059","YMLSTR":[{"value":"58.50","name":"浙能","itemStyle":[{"color":"#9297F5"}]},{"value":"21.75","name":"国能","itemStyle":[{"color":"#5CDB92"}]},{"value":"11.87","name":"华能","itemStyle":[{"color":"#E0EC84"}]},{"value":"4.74","name":"大唐","itemStyle":[{"color":"#5A69E7"}]},{"value":"0","name":"华电","itemStyle":[{"color":"#E4986C"}]},{"value":"3.14","name":"华润","itemStyle":[{"color":"#C973DF"}]},{"value":"0","name":"台塑","itemStyle":[{"color":"#38D3A0"}]},{"value":"0","name":"巨化","itemStyle":[{"color":"#95EFFF"}]}],"STATSTR":[{"cydl1":"3.95","cydl2":"4.02","jtmc":"浙能","mh1":"238.49","mh2":"247.29","name":"","qjrhl1":"6076.65","qjrhl2":"6348.20","value":"91.59"},{"cydl1":"4.20","cydl2":"3.93","jtmc":"国能","mh1":"266.07","mh2":"271.44","name":"","qjrhl1":"6784.46","qjrhl2":"6785.78","value":"92.74"},{"cydl1":"3.47","cydl2":"3.47","jtmc":"华能","mh1":"237.78","mh2":"286.14","name":"","qjrhl1":"6313.21","qjrhl2":"7582.38","value":"92.25"},{"cydl1":"5.76","cydl2":"0.00","jtmc":"大唐","mh1":"319.09","mh2":"229.03","name":"","qjrhl1":"8098.49","qjrhl2":"5865.46","value":"91.86"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"华电","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"},{"cydl1":"4.24","cydl2":"1.90","jtmc":"华润","mh1":"289.53","mh2":"0.00","name":"","qjrhl1":"7601.01","qjrhl2":"7413.83","value":"91.48"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"台塑","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"},{"cydl1":"0.00","cydl2":"0.00","jtmc":"巨化","mh1":"0.00","mh2":"0.00","name":"","qjrhl1":"0.00","qjrhl2":"0.00","value":"0"}],"SSFH":"23510.98","RJFH":"4590.23","LJFD":"539330.56"}]}]"""

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
