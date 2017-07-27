import my_appapi as appapi
import inspect
import datetime

class spotcontrol(appapi.my_appapi):

  def initialize(self):
    self.LOGLEVEL="DEBUG"
    self.log("SpotControl App")
    self.run_daily(self.timer_handler_on,datetime.time(23,30,0))
    self.run_daily(self.timer_handler_off,datetime.time(1,0,0))    

  def timer_handler_on(self,kwargs):
    self.process_event("on")

  def timer_handler_off(self,kwargs):
    self.process_event("off")

  def process_event(self,state):
    if state=="on":
      self.turn_on("input_boolean.spot")  # turn on override group first
      for entity in self.build_entity_list("group.app_spotcontrol_spots_lights",["light","switch","fan"]):
        self.log("turning on {}".format(entity))
        self.turn_on(entity)
    else:
      self.turn_off("input_boolean.spot")
      for entity in self.build_entity_list("group.app_spotcontrol_spots_lights",["light","switch","fan"]):
        self.log("turning off {}".format(entity))
        self.turn_off(entity)
