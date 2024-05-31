import openai
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

load_dotenv()

def summarize_url(url):
    api_key = os.getenv("GPT_API_KEY")
    if not api_key:
        raise ValueError("API 키를 설정하세요.")
    openai.api_key = api_key

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('title')
    title = title_tag.get_text() if title_tag else 'No Title Found'

    first_image = None
    body = soup.find('body')
    if body:
        for img in body.find_all('img'):
            img_url = img.get('src')
            if img_url:
                if not img_url.startswith('http'):
                    img_url = requests.compat.urljoin(url, img_url)
                try:
                    img_response = requests.get(img_url)
                    img = Image.open(BytesIO(img_response.content))
                    width, height = img.size
                    if width >= 400 and height >= 400:
                        first_image = img_url
                        break
                except Exception as e:
                    print(f"Error loading image: {e}")
                    continue

    image_url = first_image if first_image else 'No Image Found'

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 URL의 본문 내용을 최대 두 문장으로 요약해줘:\n\n{url}"}
        ],
        temperature=0,
        max_tokens=2048
    )

    summary = completion.choices[0].message['content'].strip()
    return {'title': title, 'summary': summary, 'url': url, 'image_url': image_url}
