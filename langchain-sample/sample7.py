# チャットモデルのラッパーをインポート
from langchain.chat_models import ChatOpenAI
# チャットモデルで利用可能なメッセージの型をインポート
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    LLMResult,
)

# チャットモデルのラッパーを初期化
chat = ChatOpenAI(temperature=0.7)

# チャットモデルに渡すメッセージを複数セット作成する
batch_messages = [
    [
        SystemMessage(content="あなたは日本語を英語に翻訳する親切なアシスタントです。"),
        HumanMessage(content="以下の文を日本語から英語に翻訳してください。「私はプログラミングが大好きです。」")
    ],
    [
        SystemMessage(content="あなたは日本語を英語に翻訳する親切なアシスタントです。"),
        HumanMessage(content="以下の文を日本語から英語に翻訳してください。「私は人工知能が大好きです。」")
    ],
]

# チャットモデルにメッセージを渡して、予測を受け取る
result: LLMResult = chat.generate(batch_messages)

# 予測結果を表示する
for generations in result.generations:
    for generation in generations:
        print(generation.text,"\n")