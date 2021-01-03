import pygame,sys,time
class WuxiaRPG(object):
	"""docstring for WuxiaRPG"""
	def __init__(self):
		super(WuxiaRPG, self).__init__()
		pygame.init()
		self.screen = pygame.display.set_mode((1024,768))
		pygame.display.set_caption("WuxiaRPG")
		self.bg = pygame.image.load("Data/Player/0.png")

if __name__ == '__main__':
	wuxiaRPG = WuxiaRPG()

