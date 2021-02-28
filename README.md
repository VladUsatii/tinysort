# tinysort

[![Twitter Follow](https://img.shields.io/twitter/follow/vladusatii.svg?style=social)](https://twitter.com/vladusatii)

[русский](https://github.com/VladUsatii/tinysort/master/README.ru.md) • [lengua española readme](https://github.com/VladUsatii/tinysort/master/README.es.md)

Made this lightweight data sorter in an airplane. I got super bored, so I put this together with Python PyQt5, NumPy, SDL2, a few random modules, and a lot of coffee. It could help you visualize 2D data (and hopefully 3D in the future) and draw pixels, as well as model shapes for ML and other types of studies.

## Install

To run on your computer, clone the repository:

```bash
git clone https://www.github.com/VladUsatii/tinysort
```

Then, simply `cd` into the directory and do the following in order:

```bash
chmod +x main.py
./main.py
```

Executing the Python application with `./main.py`, as stated above, will start the runtime process and you can then upload a supported data type.

### Forking

#### If you want to fork the project, you can download the files and edit the source code, but remember that it is run under Product. All rights reserved. Unfortunately, you can not mod our work and sell it.

## 2D Pixel Data Rendering

I used NumPy and a few other plugins to deliver a seamless visualization of pixel data. By entering data, you can render it in the 2D editor. If the application notices that there is more than two dimensional variables in a matrix (5 for its index value), it will switch to 3D Pixel Data Rendering.

To actually render a 2D pixel, do the following in a new `.txt` file:

#### example.txt
```
25 25 100 50 25
```
Let us uncover what the above pixel values draw:

* The 1st value is in charge of putting the pixel in its correct X axis value.
* The 2nd value is in charge of putting the pixel in its correct Y axis value.
* The 3rd value is in charge of setting the 'R' value in 'RGB.'
* The 4th value is in charge of setting the 'G' value in 'RGB.'
* The 5th value is in charge of setting the 'B' value in 'RGB.'

#### Remember that you can create unlimited pixel coordinates by adding more lines.

## 3D Pixel Data Rendering

I used a few visualization tools to get this correct. Unfortunately, right now, you can't enter 3D visualization points and see your item by turning it around and playing with the pixel data.

If you want to use the CSV model and train a CNN or NN with it, you can export the data to the tinysort API -- coming soon as well.

## Coloring

You can color the lines and edges of your 3D objects by clicking on them and choosing a color. You can also enter a hex code or rgb code. Below is a good example:

```python
>>> rgb(24, 10, 250)
>>> # or
>>> #141414
```

Coloring is useful for different lines or planes. If you want to add color to multiple planes, you can select them one by one or completely drag and select the region you want to change. 3D visualization does not support dragging to change color.

#### Remember that the entire Coloring toolset is coming soon and is not available right now.

## Export Shape

You can take a snapshot of the picture if the model was made primarily for capturing an image. This image is savable in either a PNG or a JPG. The image will download in your Downloads folder.

## Adding Features

I would highly appreciate the addition of new features. By forking, you can change things and let me know what can be changed for a better experience. This was really just an experiment to see how data can be rendered with _just_ points.

[Visit Product](https://www.readproduct.com/) • Read the blog [here](https://www.readproduct.com/blog/)
