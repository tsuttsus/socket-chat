# チャットモデルのラッパーをインポート
from langchain.chat_models import ChatOpenAI
# チャットプロンプト用のテンプレートをインポート
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# チャットモデルのラッパーを初期化
chat = ChatOpenAI(temperature=0)

# SystemMessage 用のテンプレートの作成
template="あなたは{input_language}を{output_language}に翻訳する親切なアシスタントです"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# HumanMessage 用のテンプレートの作成
human_template="以下の文を{input_language}から{output_language}に翻訳してください。「{text}」"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Message のテンプレートを組合わせて会話の流れを決めます
messages_template = [
    system_message_prompt,
    human_message_prompt
]

# チャットプロンプト用のテンプレートを作成します
chat_prompt_template = ChatPromptTemplate.from_messages(messages_template)

# テンプレートに具体値を組み込んでチャットプロンプトを作成します
chat_prompt = chat_prompt_template.format_prompt(input_language="日本語", output_language="英語", text="われわれは世界の変わるスピードについていけるのだろうか。").to_messages()

# チャットの補完を作成
completion = chat(chat_prompt)
print(completion.content)