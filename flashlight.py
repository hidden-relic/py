from kivy.app import App
from kivy.uix.switch import Switch
from jnius import autoclass
Camera = autoclass('android.hardware.Camera')
Parameters = autoclass('android.hardware.Camera$Parameters')
__version__ = '0.1'
class FlashApp(App):
	def build(self):
		self.root = Switch()
		self.root.bind(active=self.toggle_flash)
		self.camera = None
		return self.root
	
	def toggle_flash(self, *args):
		if self.camera == None:
			self.camera = Camera.open()
			
			print(self.camera.getParameters())
			
			
# android.permission.CAMERA

