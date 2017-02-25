import my_appapi as appapi
import inspect
import datetime

class spotcontrol(appapi.my_appapi):

  def initialize(self):
    self.LOGLEVEL="DEBUG"
    self.log("SpotControl App")
    self.run_daily(self.timer_handler_on,datetime.time(4,0,0))
    self.run_daily(self.timer_handler_off,datetime.time(5,30,0))    

  def timer_handler_on(self,kwargs):
    self.process_event("on")

  def timer_handler_off(self,kwargs):
    self.process_event("off")

  def process_event(self,state):
    light_list=[]
    light_list=self.build_light_list("group.spots_lights")
    self.log("light_list={}".format(light_list))
    if state=="on":
      for light in light_list:
        self.turn_on(light)
    else:
      for light in light_list:
        self.turn_off(light)
 
  def build_light_list(self,groupin):
    result=[]
    devtype, devname = self.split_entity(groupin)
    if devtype=="group":
      for entity in self.get_state(groupin,attribute="all")["attributes"]["entity_id"]:
        result.append(self.build_light_list(entity))
    else:
      return groupin
    return result
  
