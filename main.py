import asyncio
import os
from agents import Agent
from agents import Runner
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()


async def main():
    async with MCPServerStdio(
        params={
            "command": "npx",  # Linux環境用
            # "command": "/Users/user/.volta/bin/npx",  # MacOS環境用
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")},
        }
    ) as server:
        # サーバーからツールリストを取得
        await server.list_tools()

        # Agentの作成とMCPサーバーの設定
        agent = Agent(
            name="検索アシスタント",
            instructions="あなたは検索アシスタントです。ユーザーの質問に対して、"
            "Brave検索を使用して情報を調査し、日本語で分かりやすく回答してください。"
            "情報源も明記してください。",
            mcp_servers=[server],
        )

        # Agentの実行例
        result = await Runner.run(
            agent, "2025年にされたOpenAIの発表について教えて下さい"
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
