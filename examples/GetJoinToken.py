from src.PlugNMeet import PlugNMeet
from src.schemas.requests import JoinRoomRequest
from src.schemas.data import UserInfo, UserMetadata, DefaultLockSettings
from uuid import uuid4

async def main():
    meet_platform = PlugNMeet(base_url="http://127.0.0.1:8080", api_key="plugnmeet", api_secret="zumyyYWqv7KR2kUqvYdq4z4sXg7XTBD2ljT6")
    status, result = await meet_platform.getJoinToken(
        data=JoinRoomRequest(
            room_id="fff44422_werwe",
            user_info=UserInfo(
                name="User",
                is_admin=False,
                is_hidden=True,
                user_id=str(uuid4()),
                user_metadata=UserMetadata(
                    profile_pic="pic",
                    preferred_lang="en", # Languages: https://github.com/mynaparrot/plugNmeet-client/blob/main/src/helpers/languages.ts
                    ex_user_id="exid",
                    extra_data="None",
                    lock_settings=DefaultLockSettings(
                        lock_chat=False,
                        lock_chat_file_share=False,
                        lock_chat_send_message=True,
                        lock_screen_sharing=True
                    )
                )
            )
        )
    )
    print(f"status: {status}")
    print(f"result: {result}")
    
if __name__ == "__main__":
    from asyncio import run
    run(main())
