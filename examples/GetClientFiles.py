from src.PlugNMeet import PlugNMeet
from src.schemas.requests import GetClientFilesRequest

async def main():
    meet_platform = PlugNMeet(base_url="http://127.0.0.1:8080", api_key="plugnmeet", api_secret="zumyyYWqv7KR2kUqvYdq4z4sXg7XTBD2ljT6")
    status, result = await meet_platform.getClientFiles(data=GetClientFilesRequest())
    print(f"status: {status}")
    print(f"result: {result}")
    
if __name__ == "__main__":
    from asyncio import run
    run(main())
