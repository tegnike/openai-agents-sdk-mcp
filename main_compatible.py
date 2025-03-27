import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel

# .envファイルを読み込む
load_dotenv()

print("🔧 デバッグ情報 🔧")
print("----------------------------------------")
print(f"📍 BASE URL: {os.getenv('OPENAI_COMPATIBLE_BASE_URL')}")
print(f"🤖 使用モデル: {os.getenv('OPENAI_COMPATIBLE_MODEL')}")
print(f"🔑 API KEY設定: {'✅' if os.getenv('OPENAI_COMPATIBLE_API_KEY') else '❌'}")
print("----------------------------------------")

async def main():
    # AsyncOpenAIクライアントを初期化
    client = AsyncOpenAI(
        api_key=os.getenv("OPENAI_COMPATIBLE_API_KEY"),
        base_url=os.getenv("OPENAI_COMPATIBLE_BASE_URL"),
    )

    # OpenAIChatCompletionsModelでクライアントをラップ
    model = OpenAIChatCompletionsModel(
        model=os.getenv("OPENAI_COMPATIBLE_MODEL"),  # デフォルトはGPT-4o
        openai_client=client,
    )

    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")},
        }
    ) as server:
        # サーバーからツールリストを取得
        await server.list_tools()

        # Agentの作成（OpenAIモデルとMCPサーバーの両方を設定）
        agent = Agent(
            name="検索アシスタント",
            instructions="あなたは検索アシスタントです。ユーザーの質問に対して、"
            "Brave検索を使用して情報を調査し、日本語で分かりやすく回答してください。"
            "情報源も明記してください。",
            model=model,  # OpenAIモデルを設定
            mcp_servers=[server],  # MCPサーバーを設定
        )

        result = await Runner.run(
            agent, "2025年にされたOpenAIの発表について教えて下さい"
        )
        print("-----------------------------")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
