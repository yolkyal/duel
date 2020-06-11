import unittest
import image_manager
from unittest import mock


class TestImageManager(unittest.TestCase):
	def setUp(self):
		self.image_manager = image_manager.ImageManager()
		self.image_surface = 'IMAGE_SURFACE'
		self.image_filepath = 'IMAGE_FILEPATH'
		self.image_id = 'IMAGE_ID'

	@mock.patch('pygame.image.load')
	def testStore(self, mock_image_load):
		# WHEN
		self.image_manager.store(self.image_filepath)

		# THEN
		mock_image_load.assert_not_called()

	@mock.patch('pygame.image.load')
	def testStoreAndGet(self, mock_image_load):
		# GIVEN
		self.image_manager.store(self.image_filepath)
		mock_image_load.return_value = self.image_surface

		# WHEN
		image_surface = self.image_manager.image(self.image_filepath).get()

		# THEN
		mock_image_load.assert_called_once_with(self.image_filepath)
		image_surface = self.image_surface

	@mock.patch('pygame.image.load')
	def testStoreAndGetWithId(self, mock_image_load):
		# GIVEN
		self.image_manager.store(self.image_filepath, self.image_id)
		mock_image_load.return_value = self.image_surface

		# WHEN
		image_surface = self.image_manager.image(self.image_id).get()
		image_surface_2 = self.image_manager.image(self.image_filepath).get()

		# THEN
		mock_image_load.assert_called_once_with(self.image_filepath)
		self.assertEqual(self.image_surface, image_surface)
		self.assertEqual(None, image_surface_2)

	@mock.patch('pygame.transform.scale')
	@mock.patch('pygame.image.load')
	def testStoreAndGetWithSize(self, mock_image_load, mock_transform_scale):
		# GIVEN
		self.image_manager.store(self.image_filepath, self.image_id)
		mock_image_load.return_value = self.image_surface

		# WHEN
		self.image_manager.image(self.image_id).size((50, 50)).get()

		# THEN
		mock_image_load.assert_called_once_with(self.image_filepath)
		mock_transform_scale.assert_called_once_with(self.image_surface, (50, 50))

	@mock.patch('pygame.transform.flip')
	@mock.patch('pygame.image.load')
	def testStoreAndGetFlipped(self, mock_image_load, mock_transform_flip):
		# GIVEN
		self.image_manager.store(self.image_filepath, self.image_id)
		mock_image_load.return_value = self.image_surface

		# WHEN
		self.image_manager.image(self.image_id).flipped().get()

		# THEN
		mock_image_load.assert_called_once_with(self.image_filepath)
		mock_transform_flip.assert_called_once_with(self.image_surface, True, False)

	@mock.patch('pygame.transform.flip')
	@mock.patch('pygame.transform.scale')
	@mock.patch('pygame.image.load')
	def testStoreAndGetWithSizeFlipped(self, mock_image_load, mock_transform_scale, mock_transform_flip):
		# GIVEN
		self.image_manager.store(self.image_filepath, self.image_id)
		mock_image_load.return_value = self.image_surface
		mock_transform_scale.return_value = self.image_surface
		mock_transform_flip.return_value = self.image_surface

		# WHEN
		self.image_manager.image(self.image_id).size((50, 50)).flipped().get()

		# THEN
		mock_image_load.assert_called_once_with(self.image_filepath)
		mock_transform_scale.assert_called_once_with(self.image_surface, (50, 50))
		mock_transform_flip.assert_called_once_with(self.image_surface, True, False)


if __name__ == '__main__':
	unittest.main()