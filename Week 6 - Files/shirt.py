from PIL import Image, ImageOps
import sys
import os

def main():

    # Exactly 2 files are not provided
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]

        valid_extensions = (".jpg",".jpeg",".png")
        input_extension = os.path.splitext(input_image)[1]
        output_extension = os.path.splitext(output_image)[1]


        # Invalid Extensions
        if input_extension.lower() not in valid_extensions:
            sys.exit("File extension not supported")

        # Different Extensions
        if input_extension != output_extension:
            sys.exit("Input & output file extensions are different")

        # Edit Image
        edit_image(input_image, output_image)



def edit_image(input,output):
    try:
        # Open shirt Image
        shirt = Image.open("shirt.png")
        size = shirt.size

        with Image.open(input) as input:
            # Resize & crop input image to match size of shirt image
            input_edited = ImageOps.fit(input, size)

            # Pastes shirt image onto input_edited image
            # ( mask=shirt ) pastes only non-transparent parts of shirt image
            input_edited.paste(shirt, mask=shirt)

            # Saves edited image to specified output path
            input_edited.save(output)

    except FileNotFoundError:
        sys.exit(f"{input} doesn't exist")


if __name__ == "__main__":
    main()
