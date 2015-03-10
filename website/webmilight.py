import web
import milight
from time import sleep

BDELTA=40
ON=1
OFF=0
MAXB = 220
MINB = 20


discomode = {
    
    }
mi = milight.milight("home",udp_ip='10.1.1.12')

state = {
    1:ON,
    2:ON,
    3:ON,
    4:ON
    }
dim = {
    1:MAXB,
    2:MAXB,
    3:MAXB,
    4:MAXB
    }
white = {
    1:mi.white_ch1,
    2:mi.white_ch2,
    3:mi.white_ch3,
    4:mi.white_ch4
    }

urls = (
    '/api/(.*)/(.*)','api',
    '/', 'hello',
)




render = web.template.render('templates/')

app = web.application(urls, globals())
def sendtolight(group,action):
    action=action.lower()
    #Convert group to int and select the group of light by switching it to current state
    group = int(group)
    mi.switch(group,state[group]) 
    if (action == 'on'):
        mi.switch(group,ON)
        print "switching it on"
        state[group]=ON
    elif (action == 'off'):
        mi.switch(group,OFF)
        print "switching it off"
        state[group]=OFF
    elif (mi.color_map.has_key(action)):
        mi.col(group,mi.color_map[action])
    elif (action=="brighter"):
        if(dim[group]<MAXB):
            dim[group]+=40
            mi.dim(group,dim[group])
        else:
            mi.send(mi.max_bright)
    elif (action=="dimmer"):
        if(dim[group]>MINB):
            dim[group]-=40
            mi.dim(group,dim[group])
    elif (action=="white"):
        mi.send(white[group])
    elif (action=="disco"):
        mi.disco(0,0)
    elif (action=="init"):
        print "Init group "+str(group)
        mi.switch(group,ON)
        state[group]=ON
        sleep(0.2)
        mi.send(white[group])
        sleep(0.2)
        mi.send(mi.max_bright)
        dim[group]=MAXB
    sleep(0.1)

class hello:        
    def GET(self):
        return render.index()

class api:
    def GET(self,group,action):
        if (state.has_key(int(group))):
           sendtolight(group,action)
        return (group+' -- '+action)
   

if __name__ == "__main__":
    for i in state:
        sendtolight(i,'init')
    app.run()
