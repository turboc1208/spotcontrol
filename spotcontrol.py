import appdaemon.plugins.hass.hassapi as hass
import datetime
import time
#import my_appapi as appapi

#class spotcontrol(appapi.my_appapi):
class spotcontrol(hass.Hass):
  def initialize(self):
    self.LOGLEVEL="DEBUG"
    self.log("SpotControl App")
    self.run_in(self.timer_handler_on,3*60,target="lights.office_lights")
    self.print_schedule()
    self.log("initialization complete");
  def print_schedule(self):
    schedule=self.get_scheduler_entries()
    for app in schedule:
      self.log("schedule_entities={}".format(app))
      for handle in schedule[app]:
        self.log("{} - handle={}-{}".format(type(handle),handle,schedule[app][handle]))
        for attribute in  schedule[app][handle]:
          self.log("{}-{}".format(attribute,schedule[app][handle][attribute]))

  def timer_handler_on(self,kwargs):
    self.print_schedule()    
