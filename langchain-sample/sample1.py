from langchain.llms import OpenAI

# LLM ラッパーを初期化
llm = OpenAI(temperature=0.7)

# LLM に渡す入力テキスト
text = "カラフルな靴下を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。"

# LLM から予測を受け取って表示
prediction = llm(text)
print(prediction.strip())