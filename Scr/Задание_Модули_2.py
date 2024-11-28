from PIL import Image
import argparse

class ImageProcessor:
    # ... (код класса ImageProcessor из предыдущего примера) ...


def main():
    parser = argparse.ArgumentParser(description="Resize and rotate images.")
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("width", type=int, help="New width of the image (-1 to keep aspect ratio)")
    parser.add_argument("height", type=int, help="New height of the image (-1 to keep aspect ratio)")
    parser.add_argument("output_path", help="Path to save the output image")
    args = parser.parse_args()

    try:
        processor = ImageProcessor(args.input_path)
        processor.resize_image(args.width, args.height)
        processor.save_image(args.output_path)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()