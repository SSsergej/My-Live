from PIL import Image

class ImageProcessor:
    def __init__(self, image_path):
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        except Exception as e:
            raise Exception(f"Error opening image: {e}")


    def resize_image(self, width, height):
        """Изменяет размер изображения. Сохраняет пропорции, если один из параметров равен -1."""
        if width == -1:
            width = int(self.image.width * (height / self.image.height))
        elif height == -1:
            height = int(self.image.height * (width / self.image.width))
        self.image = self.image.resize((width, height))


    def rotate_image(self, degrees):
        """Поворачивает изображение на заданный угол."""
        self.image = self.image.rotate(degrees)


    def save_image(self, output_path):
        """Сохраняет обработанное изображение."""
        try:
            self.image.save(output_path)
            print(f"Image saved to {output_path}")
        except Exception as e:
            raise Exception(f"Error saving image: {e}")


# Пример использования:

try:
    processor = ImageProcessor("input.jpg") # Замените "input.jpg" на путь к вашему изображению

    processor.resize_image(400, -1) # Изменяем ширину на 400 пикселей, высота масштабируется пропорционально
    processor.rotate_image(90) # Поворачиваем на 90 градусов

    processor.save_image("output.jpg") # Сохраняем обработанное изображение

except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Ошибка: {e}")