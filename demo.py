# -*- coding:utf-8 -*-
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import json

res = """[{"res":"success","data":[{"SO2LIST":[{"name":"浙能集团","valueNew":"4539.77","valueOld":"5375.73"},{"name":"国能集团","valueNew":"70.17","valueOld":"95.65"},{"name":"华能集团","valueNew":"37.58","valueOld":"101.12"},{"name":"大唐集团","valueNew":"64.56","valueOld":"45.99"},{"name":"华电集团","valueNew":"","valueOld":""},{"name":"华润集团","valueNew":"21.26","valueOld":"35.81"},{"name":"台塑集团","valueNew":"","valueOld":""},{"name":"巨化集团","valueNew":"","valueOld":""}],"TITLETIME":"2022年","DUSTLIST":[{"name":"浙能集团","valueNew":"7831.45","valueOld":"5488.88"},{"name":"国能集团","valueNew":"9.23","valueOld":"8.89"},{"name":"华能集团","valueNew":"80.29","valueOld":"32.81"},{"name":"大唐集团","valueNew":"940.17","valueOld":".34"},{"name":"华电集团","valueNew":"","valueOld":""},{"name":"华润集团","valueNew":"1.38","valueOld":"2.55"},{"name":"台塑集团","valueNew":"","valueOld":""},{"name":"巨化集团","valueNew":"","valueOld":""}],"LASTYEARTAG":2021,"NOXLIST":[{"name":"浙能集团","valueNew":"5946.4","valueOld":"5668.34"},{"name":"国能集团","valueNew":"207.6","valueOld":"209.99"},{"name":"华能集团","valueNew":"95.14","valueOld":"185.18"},{"name":"大唐集团","valueNew":"157.31","valueOld":"75.41"},{"name":"华电集团","valueNew":"","valueOld":""},{"name":"华润集团","valueNew":"39.73","valueOld":"60.18"},{"name":"台塑集团","valueNew":"","valueOld":""},{"name":"巨化集团","valueNew":"","valueOld":""}],"YEARTAG":"2022","HBZKLIST":[{"crewName":"-","dates":"2022","dustPfl":"7831.45","factoryName":"-","fdl":"","groupName":"浙能集团汇总","noxPfl":"5946.4","num":"1","runTime":"","so2Pfl":"4539.77"},{"crewName":"#3","dates":"2022","dustPfl":".04","factoryName":"浙能北仑电厂","fdl":"","groupName":"浙能集团","noxPfl":"12.94","num":"2","runTime":"","so2Pfl":"6.36"},{"crewName":"#4","dates":"2022","dustPfl":".06","factoryName":"浙能北仑电厂","fdl":"","groupName":"浙能集团","noxPfl":"11.63","num":"3","runTime":"","so2Pfl":"7.4"},{"crewName":"#5","dates":"2022","dustPfl":"0","factoryName":"浙能北仑电厂","fdl":"","groupName":"浙能集团","noxPfl":"11.92","num":"4","runTime":"","so2Pfl":"7.21"},{"crewName":"#1","dates":"2022","dustPfl":"0","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":"13.53","num":"5","runTime":"","so2Pfl":"15.44"},{"crewName":"#2","dates":"2022","dustPfl":"0","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":"12.19","num":"6","runTime":"","so2Pfl":"12.3"},{"crewName":"#3","dates":"2022","dustPfl":".3","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":".01","num":"7","runTime":"","so2Pfl":".01"},{"crewName":"#4","dates":"2022","dustPfl":"0","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":"2.42","num":"8","runTime":"","so2Pfl":".59"},{"crewName":"#5","dates":"2022","dustPfl":"0","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":".64","num":"9","runTime":"","so2Pfl":"0"},{"crewName":"#6","dates":"2022","dustPfl":"0","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":"1.03","num":"10","runTime":"","so2Pfl":".06"},{"crewName":"#7","dates":"2022","dustPfl":"-","factoryName":"滨海电厂","fdl":"","groupName":"浙能集团","noxPfl":"-","num":"11","runTime":"","so2Pfl":"-"},{"crewName":"#1","dates":"2022","dustPfl":"0","factoryName":"长兴电厂","fdl":"","groupName":"浙能集团","noxPfl":"4.84","num":"12","runTime":"","so2Pfl":"3.63"},{"crewName":"#2","dates":"2022","dustPfl":"0","factoryName":"长兴电厂","fdl":"","groupName":"浙能集团","noxPfl":"5.96","num":"13","runTime":"","so2Pfl":"3.93"},{"crewName":"#3","dates":"2022","dustPfl":".08","factoryName":"长兴电厂","fdl":"","groupName":"浙能集团","noxPfl":"5.83","num":"14","runTime":"","so2Pfl":"4.43"},{"crewName":"#4","dates":"2022","dustPfl":"0","factoryName":"长兴电厂","fdl":"","groupName":"浙能集团","noxPfl":"6.18","num":"15","runTime":"","so2Pfl":"4.08"},{"crewName":"#1","dates":"2022","dustPfl":"0","factoryName":"嘉兴电厂","fdl":"","groupName":"浙能集团","noxPfl":"33.83","num":"16","runTime":"","so2Pfl":"11.23"},{"crewName":"#2","dates":"2022","dustPfl":"0","factoryName":"嘉兴电厂","fdl":"","groupName":"浙能集团","noxPfl":"5.82","num":"17","runTime":"","so2Pfl":"2.47"},{"crewName":"#3","dates":"2022","dustPfl":".01","factoryName":"嘉华电厂","fdl":"","groupName":"浙能集团","noxPfl":"22.5","num":"18","runTime":"","so2Pfl":"7.15"},{"crewName":"#4","dates":"2022","dustPfl":"0","factoryName":"嘉华电厂","fdl":"","groupName":"浙能集团","noxPfl":"13.15","num":"19","runTime":"","so2Pfl":"5.96"},{"crewName":"#5","dates":"2022","dustPfl":"0","factoryName":"嘉华电厂","fdl":"","groupName":"浙能集团","noxPfl":"60.19","num":"20","runTime":"","so2Pfl":"21.42"},{"crewName":"#6","dates":"2022","dustPfl":".06","factoryName":"嘉华电厂","fdl":"","groupName":"浙能集团","noxPfl":"65.97","num":"21","runTime":"","so2Pfl":"21.92"},{"crewName":"#7","dates":"2022","dustPfl":"0","factoryName":"嘉华电厂","fdl":"","groupName":"浙能集团","noxPfl":"134.81","num":"22","runTime":"","so2Pfl":"39.5"},{"crewName":"#8","dates":"2022","dustPfl":".02","factoryName":"嘉华电厂","fdl":"","groupName":"浙能集团","noxPfl":"76.04","num":"23","runTime":"","so2Pfl":"12.99"},{"crewName":"#1","dates":"2022","dustPfl":"0","factoryName":"兰溪电厂","fdl":"","groupName":"浙能集团","noxPfl":"14.92","num":"24","runTime":"","so2Pfl":"9.58"},{"crewName":"#2","dates":"2022","dustPfl":".68","factoryName":"兰溪电厂","fdl":"","groupName":"浙能集团","noxPfl":"14.1","num":"25","runTime":"","so2Pfl":"8.83"},{"crewName":"#3","dates":"2022","dustPfl":".07","factoryName":"兰溪电厂","fdl":"","groupName":"浙能集团","noxPfl":"14.31","num":"26","runTime":"","so2Pfl":"8.57"},{"crewName":"#4","dates":"2022","dustPfl":"1.12","factoryName":"兰溪电厂","fdl":"","groupName":"浙能集团","noxPfl":"13.48","num":"27","runTime":"","so2Pfl":"8.28"},{"crewName":"#1","dates":"2022","dustPfl":".25","factoryName":"乐清电厂","fdl":"","groupName":"浙能集团","noxPfl":"6.39","num":"28","runTime":"","so2Pfl":"5.94"},{"crewName":"#2","dates":"2022","dustPfl":"27.95","factoryName":"乐清电厂","fdl":"","groupName":"浙能集团","noxPfl":"-47.45","num":"29","runTime":"","so2Pfl":"2.81"},{"crewName":"#3","dates":"2022","dustPfl":".12","factoryName":"乐清电厂","fdl":"","groupName":"浙能集团","noxPfl":"10.51","num":"30","runTime":"","so2Pfl":"6.59"},{"crewName":"#4","dates":"2022","dustPfl":"10.73","factoryName":"乐清电厂","fdl":"","groupName":"浙能集团","noxPfl":"6","num":"31","runTime":"","so2Pfl":".49"},{"crewName":"#7","dates":"2022","dustPfl":"0","factoryName":"台州电厂","fdl":"","groupName":"浙能集团","noxPfl":"6.57","num":"32","runTime":"","so2Pfl":"4.16"},{"crewName":"#8","dates":"2022","dustPfl":"1.53","factoryName":"台州电厂","fdl":"","groupName":"浙能集团","noxPfl":"447.27","num":"33","runTime":"","so2Pfl":"53.63"},{"crewName":"#9","dates":"2022","dustPfl":"14.98","factoryName":"台州电厂","fdl":"","groupName":"浙能集团","noxPfl":"-.56","num":"34","runTime":"","so2Pfl":"-.62"},{"crewName":"#10","dates":"2022","dustPfl":"0","factoryName":"台州电厂","fdl":"","groupName":"浙能集团","noxPfl":"2.71","num":"35","runTime":"","so2Pfl":"1.34"},{"crewName":"#3","dates":"2022","dustPfl":"0","factoryName":"特鲁莱电厂","fdl":"","groupName":"浙能集团","noxPfl":"5.44","num":"36","runTime":"","so2Pfl":"2.86"},{"crewName":"#4","dates":"2022","dustPfl":"0","factoryName":"特鲁莱电厂","fdl":"","groupName":"浙能集团","noxPfl":"9.41","num":"37","runTime":"","so2Pfl":"4.13"},{"crewName":"#5","dates":"2022","dustPfl":"0","factoryName":"温州电厂","fdl":"","groupName":"浙能集团","noxPfl":"7.19","num":"38","runTime":"","so2Pfl":"3.28"},{"crewName":"#6","dates":"2022","dustPfl":"0","factoryName":"温州电厂","fdl":"","groupName":"浙能集团","noxPfl":"8.52","num":"39","runTime":"","so2Pfl":"4.6"},{"crewName":"#7","dates":"2022","dustPfl":".05","factoryName":"温州电厂","fdl":"","groupName":"浙能集团","noxPfl":"12.63","num":"40","runTime":"","so2Pfl":"6.21"},{"crewName":"#8","dates":"2022","dustPfl":".19","factoryName":"温州电厂","fdl":"","groupName":"浙能集团","noxPfl":"11.35","num":"41","runTime":"","so2Pfl":"4.83"},{"crewName":"#1","dates":"2022","dustPfl":"1.01","factoryName":"六横电厂","fdl":"","groupName":"浙能集团","noxPfl":"29.14","num":"42","runTime":"","so2Pfl":"13.21"},{"crewName":"#2","dates":"2022","dustPfl":"93.8","factoryName":"六横电厂","fdl":"","groupName":"浙能集团","noxPfl":"123","num":"43","runTime":"","so2Pfl":"109.47"},{"crewName":"#1","dates":"2022","dustPfl":".39","factoryName":"台二电厂","fdl":"","groupName":"浙能集团","noxPfl":"19","num":"44","runTime":"","so2Pfl":"10.36"},{"crewName":"#2","dates":"2022","dustPfl":"7678.01","factoryName":"台二电厂","fdl":"","groupName":"浙能集团","noxPfl":"4731.04","num":"45","runTime":"","so2Pfl":"4083.14"},{"crewName":"-","dates":"2022","dustPfl":"9.23","factoryName":"-","fdl":"","groupName":"国能集团汇总","noxPfl":"207.6","num":"46","runTime":"","so2Pfl":"70.17"},{"crewName":"#1","dates":"2022","dustPfl":"0","factoryName":"宁海电厂","fdl":"","groupName":"国能集团","noxPfl":"20.52","num":"47","runTime":"","so2Pfl":"0"},{"crewName":"#2","dates":"2022","dustPfl":"0","factoryName":"宁海电厂","fdl":"","groupName":"国能集团","noxPfl":"12.04","num":"48","runTime":"","so2Pfl":"5.47"},{"crewName":"#3","dates":"2022","dustPfl":"4.47","factoryName":"宁海电厂","fdl":"","groupName":"国能集团","noxPfl":"24.19","num":"49","runTime":"","so2Pfl":"10.27"},{"crewName":"#4","dates":"2022","dustPfl":"0","factoryName":"宁海电厂","fdl":"","groupName":"国能集团","noxPfl":"9.34","num":"50","runTime":"","so2Pfl":"3.54"},{"crewName":"#5","dates":"2022","dustPfl":"1.11","factoryName":"宁海电厂","fdl":"","groupName":"国能集团","noxPfl":"17.79","num":"51","runTime":"","so2Pfl":"8.15"},{"crewName":"#6","dates":"2022","dustPfl":".81","factoryName":"宁海电厂","fdl":"","groupName":"国能集团","noxPfl":"22.62","num":"52","runTime":"","so2Pfl":"11.23"},{"crewName":"#1","dates":"2022","dustPfl":".14","factoryName":"北仑第一电厂","fdl":"","groupName":"国能集团","noxPfl":"13.46","num":"53","runTime":"","so2Pfl":"4.11"},{"crewName":"#2","dates":"2022","dustPfl":".65","factoryName":"北仑第一电厂","fdl":"","groupName":"国能集团","noxPfl":"15.95","num":"54","runTime":"","so2Pfl":"4.77"},{"crewName":"#6","dates":"2022","dustPfl":".87","factoryName":"北仑第三电厂","fdl":"","groupName":"国能集团","noxPfl":"28.17","num":"55","runTime":"","so2Pfl":"7.42"},{"crewName":"#7","dates":"2022","dustPfl":"1.18","factoryName":"北仑第三电厂","fdl":"","groupName":"国能集团","noxPfl":"29.28","num":"56","runTime":"","so2Pfl":"9.8"},{"crewName":"#3","dates":"2022","dustPfl":"0","factoryName":"舟山电厂","fdl":"","groupName":"国能集团","noxPfl":"4.32","num":"57","runTime":"","so2Pfl":"5.33"},{"crewName":"#4","dates":"2022","dustPfl":"0","factoryName":"舟山电厂","fdl":"","groupName":"国能集团","noxPfl":"9.92","num":"58","runTime":"","so2Pfl":".08"},{"crewName":"-","dates":"2022","dustPfl":"80.29","factoryName":"-","fdl":"","groupName":"华能集团汇总","noxPfl":"95.14","num":"59","runTime":"","so2Pfl":"37.58"},{"crewName":"#1","dates":"2022","dustPfl":"1.38","factoryName":"玉环电厂","fdl":"","groupName":"华能集团","noxPfl":"32.03","num":"60","runTime":"","so2Pfl":"14.21"},{"crewName":"#2","dates":"2022","dustPfl":".68","factoryName":"玉环电厂","fdl":"","groupName":"华能集团","noxPfl":"16.62","num":"61","runTime":"","so2Pfl":"8.8"},{"crewName":"#3","dates":"2022","dustPfl":"2.51","factoryName":"玉环电厂","fdl":"","groupName":"华能集团","noxPfl":"25.79","num":"62","runTime":"","so2Pfl":"13.38"},{"crewName":"#4","dates":"2022","dustPfl":"2.66","factoryName":"玉环电厂","fdl":"","groupName":"华能集团","noxPfl":"33.1","num":"63","runTime":"","so2Pfl":"19.94"},{"crewName":"#1","dates":"2022","dustPfl":"0","factoryName":"华能长兴电厂","fdl":"","groupName":"华能集团","noxPfl":"12.48","num":"64","runTime":"","so2Pfl":"6.2"},{"crewName":"#2","dates":"2022","dustPfl":"73.06","factoryName":"华能长兴电厂","fdl":"","groupName":"华能集团","noxPfl":"-24.88","num":"65","runTime":"","so2Pfl":"-24.95"},{"crewName":"-","dates":"2022","dustPfl":"940.17","factoryName":"-","fdl":"","groupName":"大唐集团汇总","noxPfl":"157.31","num":"66","runTime":"","so2Pfl":"64.56"},{"crewName":"#1","dates":"2022","dustPfl":"938.79","factoryName":"乌沙山电厂","fdl":"","groupName":"大唐集团","noxPfl":"119.2","num":"67","runTime":"","so2Pfl":"37.62"},{"crewName":"#2","dates":"2022","dustPfl":".03","factoryName":"乌沙山电厂","fdl":"","groupName":"大唐集团","noxPfl":"11.69","num":"68","runTime":"","so2Pfl":"8.44"},{"crewName":"#3","dates":"2022","dustPfl":"1.29","factoryName":"乌沙山电厂","fdl":"","groupName":"大唐集团","noxPfl":"16.07","num":"69","runTime":"","so2Pfl":"11.18"},{"crewName":"#4","dates":"2022","dustPfl":".06","factoryName":"乌沙山电厂","fdl":"","groupName":"大唐集团","noxPfl":"10.35","num":"70","runTime":"","so2Pfl":"7.32"},{"crewName":"-","dates":"2022","dustPfl":"-","factoryName":"-","fdl":"","groupName":"华电集团汇总","noxPfl":"-","num":"71","runTime":"","so2Pfl":"-"},{"crewName":"-","dates":"2022","dustPfl":"-","factoryName":"-","fdl":"","groupName":"华电集团","noxPfl":"-","num":"72","runTime":"","so2Pfl":"-"},{"crewName":"-","dates":"2022","dustPfl":"1.38","factoryName":"-","fdl":"","groupName":"华润集团汇总","noxPfl":"39.73","num":"73","runTime":"","so2Pfl":"21.26"},{"crewName":"#1","dates":"2022","dustPfl":".54","factoryName":"苍南电厂","fdl":"","groupName":"华润集团","noxPfl":"23.7","num":"74","runTime":"","so2Pfl":"12.32"},{"crewName":"#2","dates":"2022","dustPfl":".84","factoryName":"苍南电厂","fdl":"","groupName":"华润集团","noxPfl":"16.03","num":"75","runTime":"","so2Pfl":"8.94"},{"crewName":"-","dates":"2022","dustPfl":"-","factoryName":"-","fdl":"","groupName":"台塑集团汇总","noxPfl":"-","num":"76","runTime":"","so2Pfl":"-"},{"crewName":"#1","dates":"2022","dustPfl":"-","factoryName":"台塑电厂","fdl":"","groupName":"台塑集团","noxPfl":"-","num":"77","runTime":"","so2Pfl":"-"},{"crewName":"#2","dates":"2022","dustPfl":"-","factoryName":"台塑电厂","fdl":"","groupName":"台塑集团","noxPfl":"-","num":"78","runTime":"","so2Pfl":"-"},{"crewName":"#3","dates":"2022","dustPfl":"-","factoryName":"台塑电厂","fdl":"","groupName":"台塑集团","noxPfl":"-","num":"79","runTime":"","so2Pfl":"-"},{"crewName":"-","dates":"2022","dustPfl":"-","factoryName":"-","fdl":"","groupName":"巨化集团汇总","noxPfl":"-","num":"80","runTime":"","so2Pfl":"-"},{"crewName":"#9","dates":"2022","dustPfl":"-","factoryName":"巨宏电厂","fdl":"","groupName":"巨化集团","noxPfl":"-","num":"81","runTime":"","so2Pfl":"-"}],"RUNTIMELIST":[{"name":"浙能集团","valueNew":"280007.35","valueOld":"324952.81"},{"name":"国能集团","valueNew":"81220.71","valueOld":"92365.51"},{"name":"华能集团","valueNew":"38470.32","valueOld":"46946.74"},{"name":"大唐集团","valueNew":"24441.96","valueOld":"28509.45"},{"name":"华电集团","valueNew":"","valueOld":""},{"name":"华润集团","valueNew":"12425.09","valueOld":"14719.1"},{"name":"台塑集团","valueNew":"15947.89","valueOld":"19031.67"},{"name":"巨化集团","valueNew":"","valueOld":""}]}]}]"""

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081", "http://127.0.0.1:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/jndpportal/wbjk/getHbzkStat.xhtml")
async def home():
    return json.loads(res)


if __name__ == "__main__":
    uvicorn.run("demo:app", host="localhost", port=8080, reload=True)
