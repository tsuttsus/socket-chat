# ソケット通信(サーバー側)
import socket
from langchain.llms import OpenAI

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


host1 = '127.0.0.1'
port1 = 8765

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind((host1, port1))
socket1.listen(1)

print('クライアントからの入力待ち状態')

# コネクションとアドレスを取得
connection, address = socket1.accept()
print('接続したクライアント情報:'  + str(address))

# 無限ループ　byeの入力でループを抜ける
recvline = ''
sendline = ''
num = 0
while True:

    # クライアントからデータを受信
    recvline = connection.recv(4096).decode()

    if recvline == 'bye':
        break

    try:
        # LLM に渡す入力テキスト
        text = recvline

        # LLM から予測を受け取って表示
        #prediction = llm(text)
        prediction = conversation.predict(input=text)
        sendline = str(prediction.strip()).encode('utf-8')
        #num = int(recvline)
        #if num % 2 == 0:
        #    sendline = 'OKです'.encode('utf-8')
        #else:
        #    sendline = 'NGです'.encode('utf-8')

        connection.send(sendline)

    except ValueError as e:
        # 送信用の文字を送信
        sendline = '入力して下さい'.encode('utf-8')
        connection.send(sendline)
    finally:
        print('クライアントで入力された文字＝' + str(recvline))
        
# クローズ
connection.close()
socket1.close()
print('サーバー側終了です')