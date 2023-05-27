from typing import Dict, List

# LLMChain のインポート
from langchain.chains import LLMChain

# カスタムチェーンを定義するために Chain クラスをインポート
from langchain.chains.base import Chain


# このチェーンは、２つの LLMChain の出力を連結する
class ConcatenateChain(Chain):
    # もととなる２つの LLMChain をコンストラクタで受け取る
    chain_1: LLMChain
    chain_2: LLMChain

    @property
    def input_keys(self) -> List[str]:
        # ２つのチェーンの入力キーの和集合
        all_input_vars = set(self.chain_1.input_keys).union(set(self.chain_2.input_keys))
        return list(all_input_vars)

    @property
    def output_keys(self) -> List[str]:
        # このチェーンの出力キーは、concat_output のみ
        return ['concat_output']

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        # `output_keys` で定義したキーをもつ Dict を返す関数を定義する
        # ここでは、２つのチェーンを独立に実行した得られた出力を連結して返す
        output_1 = self.chain_1.run(inputs)
        output_2 = self.chain_2.run(inputs)
        return {'concat_output': output_1 + output_2}

# llm ラッパーのインポート
from langchain import OpenAI
# LLM チェーンの構築で必要なプロンプトテンプレートのインポート
from langchain.prompts import PromptTemplate

# llm ラッパーの初期化
llm = OpenAI(temperature=0)

prompt_1 = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。",
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1)

prompt_2 = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社のスローガンとして、何かいいものはないですか？日本語でお願いします。",
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

concat_chain = ConcatenateChain(chain_1=chain_1, chain_2=chain_2)
concat_output = concat_chain.run("ドカ食い唐揚げ定食")
print(f"Concatenated output:\n{concat_output}")
