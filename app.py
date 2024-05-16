#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

if __name__ == "__main__":
    text = "Hello dear reader, you are very dear!"
    print("Generating image")
    wordcloud = WordCloud().generate(text)

    # lower max_font_size
    # wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # image = wordcloud.to_image()
    # image.show()
