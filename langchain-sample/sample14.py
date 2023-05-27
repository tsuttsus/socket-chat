# ドキュメントローダーをインポート
from langchain.document_loaders import TextLoader
# ドキュメントローダーの初期化
loader = TextLoader('bocchan.txt')

# インデックスの作成に用いるクラスをインポート
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper

# ベクターストアの作成
index: VectorStoreIndexWrapper = VectorstoreIndexCreator().from_loaders([loader])

query = "主人公の職業は？"
answer = index.query(query)

print(answer)