import openai
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

def summarize_url(url):
    # API 키 가져오기
    api_key = os.getenv("GPT_API_KEY")

    if not api_key:
        raise ValueError("API 키를 설정하세요.")

    # OpenAI API에 키 설정
    openai.api_key = api_key

    # Chat GPT API 호출하여 요약 요청
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"다음 URL의 title 태그의 내용 그 자체와 최대 두 문장으로 요약된 본문 내용을 각각 title, content에 저장한 json 형식으로 반환해줘:\n\n{url}"}
        ],
        temperature=0,
        max_tokens=2048
    )

    # 요약된 내용 반환
    summary = completion.choices[0].message['content'].strip()
    return summary
