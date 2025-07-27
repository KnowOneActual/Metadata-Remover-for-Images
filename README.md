

# 🖼️ Metadata Remover for Images

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Metadata Remover for Images**! This helpful Python script lets you easily strip metadata from your image files, which is great for protecting your privacy when you share photos online.

## ✨ What It Does

* **Processes Single Images**: Quickly remove metadata from any image file you specify.
* **Simple to Use**: It will ask you for the file paths, making it straightforward to get started.
* **Smart Validation**: Ensures your output file has a valid image extension.

## 💡 How It Works

This script uses the **Pillow** library for all its image processing magic. When you run it, you'll be prompted to provide two things:

1.  The location of the image file you want to clean up.
2.  Where you'd like to save the new image, free of metadata.

Once you provide that information, the script creates a fresh version of your image without any extra metadata attached.

## 📦 Getting Started

First, make sure you have the Pillow library installed. If not, you can install it easily with pip:

```bash
pip install Pillow
````

## 🚀 How to Use

1.  Download the script to your computer.

2.  Open your terminal or command prompt and run the script using Python:

    ```bash
    python metadata_remover.py
    ```

3.  Follow the prompts to enter your input and output file paths.

That's it\! You'll have a clean image ready to go.

## 📝 Example

Here’s what it looks like when you run it:

```bash
python metadata_remover.py
```

```
Enter the path to the image file: /path/to/your/photo.jpg
Enter the path to save the image without metadata: /path/to/your/photo_no_metadata.jpg
```

## Why Remove Metadata?

Image metadata can sometimes contain sensitive details like where a photo was taken, what camera was used, and other specific information. By removing this, you gain more control over what data you share and help safeguard your privacy.

## 📄 License

This project operates under the MIT License. You can find all the details in the [LICENSE](https://www.google.com/search?q=LICENSE) file. This means you're free to use, modify, and distribute the software with certain conditions, including keeping the copyright and permission notices intact. The software is provided "as is," without any warranty, and the authors or copyright holders are not liable for any damages arising from its use.

