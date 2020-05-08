from django.shortcuts import render
from django.http import HttpResponse
from .models import sheet
from WindPy import w
w.start()
import json
import datetime


# Create your views here.

def index(request):
    return render(request, 'index.html')


def data_k(request):
    return render(request, 'data_k.html')





def data_tree(request):

    def get_wind():

        data = []
        date_str = str(datetime.date.today())
        #sw = w.wss(
        #    "801010.SI,801020.SI,801030.SI,801040.SI,801050.SI,801080.SI,801110.SI,801120.SI,801130.SI,801140.SI,801150.SI,801160.SI,801170.SI,801180.SI,801200.SI,801210.SI,801230.SI,801710.SI,801720.SI,801730.SI,801740.SI,801750.SI,801760.SI,801770.SI,801780.SI,801790.SI,801880.SI,801890.SI",
        #    "sec_name,pct_chg", "tradeDate=" + date_str + ";cycle=D", usedf = True)[1]
        sw = w.wsq(
            "801010.SI,801020.SI,801030.SI,801040.SI,801050.SI,801080.SI,801110.SI,801120.SI,801130.SI,801140.SI,801150.SI,801160.SI,801170.SI,801180.SI,801200.SI,801210.SI,801230.SI,801710.SI,801720.SI,801730.SI,801740.SI,801750.SI,801760.SI,801770.SI,801780.SI,801790.SI,801880.SI,801890.SI",
            "rt_pct_chg_1min", usedf=True)[1]
        name = ['农林牧渔(申万)', '采掘(申万)', '化工(申万)', '钢铁(申万)', '有色金属(申万)', '电子(申万)', '家用电器(申万)', '食品饮料(申万)', '纺织服装(申万)', '轻工制造(申万)', '医药生物(申万)', '公用事业(申万)', '交通运输(申万)', '房地产(申万)', '商业贸易(申万)', '休闲服务(申万)', '综合(申万)', '建筑材料(申万)', '建筑装饰(申万)', '电气设备(申万)', '国防军工(申万)', '计算机(申万)', '传媒(申万)', '通信(申万)', '银行(申万)', '非银金融(申万)', '汽车(申万)', '机械设备(申万)']
        for i, j in zip(name, sw.RT_PCT_CHG_1MIN.tolist()):
            data.append({'name': i, 'value': j+1})
        return data
    data = get_wind()

    #data_example
    temp0 = [{'name': '农林牧渔', 'value': - 0.5439494843812146},
             {'name': '采掘', 'value': 1.0458692134375789},
             {'name': '化工', 'value': 0.8631603584562461},
             {'name': '钢铁', 'value': 1.760225726607722},
             {'name': '有色金属', 'value': 1.4120883370717672},
             {'name': '电子', 'value': 5.273509184471566},
             {'name': '家用电器', 'value': 2.5933290691045823},
             {'name': '食品饮料', 'value': 2.9473781945012574},
             {'name': '纺织服装', 'value': - 2.544023027429718},
             {'name': '轻工制造', 'value': 1.83962181409952},
             {'name': '医药生物', 'value': - 0.297971147564141},
             {'name': '公用事业', 'value': 1.1301394684254749},
             {'name': '交通运输', 'value': 1.1142815200836726},
             {'name': '房地产', 'value': 1.3629744971998945},
             {'name': '商业贸易', 'value': 1.4073361997286016},
             {'name': '休闲服务', 'value': 3.578829429073359},
             {'name': '综合', 'value': 0.809522381794745},
             {'name': '建筑材料', 'value': 3.2333846472884535},
             {'name': '建筑装饰', 'value': 2.99198702661452},
             {'name': '电气设备', 'value': 3.243125679664434},
             {'name': '国防军工', 'value': 4.2533706436021435},
             {'name': '计算机', 'value': 2.981114406118307},
             {'name': '通信', 'value': 6.639672252603171},
             {'name': '银行', 'value': 1.0920441330471358},
             {'name': '非银金融', 'value': 2.401450380923144},
             {'name': '汽车', 'value': 2.724303905742058},
             {'name': '机械设备', 'value': 1.8375186096054283}]

    #return render(request, 'data_tree.html', context={'data': json.dumps(temp0, ensure_ascii=False)})
    return render(request, 'data_tree.html', context={'data': json.dumps(data, ensure_ascii=False)})
