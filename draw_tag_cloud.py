from wordcloud import WordCloud
import matplotlib.pyplot as plt
from yaspin import yaspin


def draw_tag_cloud(tags, show: bool):
    # lower max_font_size
    # wordcloud = WordCloud(max_font_size=40).generate(text)
    with yaspin(text="Generating tag text"):
        tag_text = " ".join(tags)
    with yaspin(text="Generating tag cloud"):
        wordcloud = WordCloud(
            width=1920,
            height=1080,
            collocations=False
        ).generate(tag_text)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if show:
        plt.show()
