# conda install -n hface -c conda-forge python-dotenv
from dotenv import find_dotenv, load_dotenv
# conda install -n hface -c huggingface transformers
from transformers import pipeline

load_dotenv(find_dotenv())


def image2text(url):
    image_to_text = pipeline(
        'image-to-text',
        model='Salesforce/blip-image-captioning-base'
    )
    text = image_to_text(url)[0]['generated_text']
    print(text)
    return(text)


if __name__ == '__main__':
    image2text(url="images/image1.jpeg")
