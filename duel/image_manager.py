import pygame

class ImageManager:
	def __init__(self):
		self.images = {}

	def store(self, image_filepath, image_id=None):
		self.images[image_id if image_id else image_filepath] = image_filepath

	def image(self, image_id):
		return ImageGetParams(self, image_id)

	def get(self, image_id, flipped=False, size=None):
		image_filepath = self.images.get(image_id, None)
		if image_filepath:
			image = pygame.image.load(image_filepath)
			if image:
				if flipped:
					image = pygame.transform.flip(image, True, False)
				if size:
					image = pygame.transform.scale(image, size)
				return image


class ImageGetParams:
	def __init__(self, image_manager, image_id, flipped=False, size=None):
		self.image_manager = image_manager
		self.image_id = image_id
		self._flipped = flipped
		self._size = size

	def flipped(self):
		return ImageGetParams(self.image_manager, self.image_id, True, self._size)

	def size(self, size):
		return ImageGetParams(self.image_manager, self.image_id, self._flipped, size)

	def get(self):
		return self.image_manager.get(self.image_id, self._flipped, self._size)
