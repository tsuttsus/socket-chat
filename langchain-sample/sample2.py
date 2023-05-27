# `PromptTemplate` をインポート
from langchain.prompts import PromptTemplate

# プロンプトテンプレートの作成
prompt = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。",
)

# テンプレートからプロンプトを作成
prompt = prompt.format(product="カラフルな靴下")
print(prompt)