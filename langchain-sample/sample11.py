# チャットモデルのラッパーをインポート
from langchain.chat_models import ChatOpenAI

# 会話をしたりメモリから文脈を読み込むチェーン
from langchain.chains import ConversationChain

# チャット履歴のラッパーをインポート
from langchain.memory import ConversationBufferMemory

# List[BaseMessage] 型のメッセージ一覧を辞書型に変換するのに使うメソッドをインポート
from langchain.schema import messages_to_dict

# チャットプロンプト用のテンプレートをインポート
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder, 
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 言語モデルのラッパーを初期化
chat = ChatOpenAI(temperature=0.7)

# メモリオブジェクトを作成
# メモリに「return_messages=True」を指定すると、文字列でなくList[ChatMessage]を返すように指示できます
memory = ConversationBufferMemory(return_messages=True)

# システムメッセージ用のテンプレートを作成
template = """
以下は、人間とAIのフレンドリーな会話です。
AIは饒舌で、その文脈から具体的な内容をたくさん教えてくれます。
AIは質問の答えを知らない場合、正直に「知らない」と答えます。
"""

# プロンプトテンプレートを作成
# チャットプロンプトテンプレートに `MessagesPlaceholder` を追加することで、
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(template),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# 会話用のチェーンを作成
# 初期化時に、使用するチャットモデル、メモリオブジェクト、プロンプトテンプレートを指定します
conversation = ConversationChain(llm=chat, memory=memory, prompt=prompt)

# 会話を開始します
command = input("You: ")

while True: 
  response = conversation.predict(input=command)
  print(f"AI: {response}")
  command = input("You: ")
  if command == "exit":
    break

# 最後に、実際に会話した内容が memory オブジェクトに保持されていることを確認します
history = memory.chat_memory
messages = json.dumps(messages_to_dict(history.messages), indent=2, ensure_ascii=False)
print(f"memory: {messages}")