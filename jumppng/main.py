import os
import sys
from PIL import Image

app_version = "0.2.1"


def display_help():
    help_message = r"""
    --- Welcome ---
    
    Hi, I'm Alireza Fazeli, and I created this application with love.
    This application is designed to make your life easier. Please follow my LinkedIn and GitHub:
    https://linkedin.com/in/alirezafazeli
    https://github.com/alirezafazeli8
    
    What do you need?
    
    You need two paths: 
    1. The path to your JPEG file.
       Example: "D:\\3- photo\\yakuza.jpg"
    2. The destination path where you want to save the PNG.
       Example: "C:\\Users\\Alireza\\Desktop"
       
    Commands:
    -c, --convert : Convert your JPEG file to PNG.
                    Example: python JpegToPngConverter.py -c "D:\\3- photo\\yakuza.jpg" "C:\\Users\\Alireza\\Desktop"
                    
    -h, --help : Display this help message.
    
    -v : Show the current version of the application.
    
    Bye bye :))))
    
    ---------------
    """
    print(help_message)


def convert_image(file_path, save_file_path):
    try:
        # Open user image
        user_image = Image.open(file_path)

        # Extract base filename and create PNG path
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        png_file_path = os.path.join(save_file_path, f"{file_name}.png")

        # Save image as PNG
        user_image.save(png_file_path, "PNG")

        print(
            f"""
        -- DONE ---
        Your file has been saved at: {png_file_path}
        -----------
        """
        )

    except FileNotFoundError:
        print(
            """
        -- Error --
        I can't find the file. Please insert a correct file path.
        Use -h or --help to know how to work.
        -----------
        """
        )
    except Exception as e:
        print(
            f"""
        -- Error --
        An unexpected error occurred: {e}
        -----------
        """
        )


def main():
    try:
        if len(sys.argv) == 3:
            raise Exception
        elif len(sys.argv) < 2:
            raise IndexError

        command = sys.argv[1]

        if command in ("-h", "--help"):
            display_help()

        elif command in ("-c", "--convert") and len(sys.argv) == 4:
            file_path = sys.argv[2]
            save_file_path = sys.argv[3]
            convert_image(file_path, save_file_path)

        elif command in ("-v", "--version"):
            print(
                f"""
            --- Hi ---
            We are in the first step, and I'm currently at version {app_version}.
            --------
            """
            )

        else:
            print(
                """
            --- Error ---
            Invalid command. Use -h or --help for help.
            -------------
            """
            )

    # Specific for windows users : handle error for cant find save file path
    except Exception:
        # find file path
        file_path = sys.argv[2]

        # make jumppng save file path
        save_file_path = f"C:\\Users\\{os.getlogin()}\\Pictures\\jumppng\\"

        # check folder exist or not if not exist create new jumppng folder
        if os.path.exists(save_file_path):
            convert_image(file_path, save_file_path)
        else:
            os.makedirs(save_file_path)
            convert_image(file_path, save_file_path)

    except IndexError:
        print(
            """
        --- Invalid Command ---
        Use -h or --help for help.
        ---------------------
        """
        )


if __name__ == "__main__":
    main()
