
import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

bot = Bot()

my_friend = bot.friends().search('Daybreak', sex=MALE, city="北京")[0]
my_friend.send("你好？")


@bot.register(my_friend)
def step1 (msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        result = stats_word.stats_text_cn(content,10)
     
        result_dict = {}
        for i in result:
            result_dict[i[0]]=i[1]       
               
        plt.rcdefaults()
        fig,ax = plt.subplots() 
        
        keys=tuple(result_dict.keys())
        values=tuple(result_dict.values())
        y_pos = np.arange(len(keys)) #y轴词的个数
        
        
        ax.barh(y_pos,values,align='center',color='blue',ecolor='black')
        

        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys,fontproperties="SimHei")
        ax.invert_yaxis()
        ax.set_xlabel(u'次数',fontproperties="SimHei")
        ax.set_title(u'前10词频统计图',fontproperties="SimHei")
        
        plt.savefig('Day13.png')
        plt.show('Day13.png')
        msg.reply_image('Day13.png')

embed()
