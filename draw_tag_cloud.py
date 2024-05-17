from wordcloud import WordCloud
import matplotlib.pyplot as plt


def draw_tag_cloud(tags, show: bool):
    # lower max_font_size
    # wordcloud = WordCloud(max_font_size=40).generate(text)
    wordcloud = WordCloud().generate(" ".join(tags))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if show:
        plt.show()
