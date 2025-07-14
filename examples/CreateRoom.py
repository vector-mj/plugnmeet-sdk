from plugnmeet_sdk import PlugNMeet
from plugnmeet_sdk.schemas.requests import CreateRoomRequest

async def main():
    meet_platform = PlugNMeet(base_url="http://127.0.0.1:8080", api_key="plugnmeet", api_secret="zumyyYWqv7KR2kUqvYdq4z4sXg7XTBD2ljT6")
    data = {
        "room_id": "123456",
        "max_participants": 5,
        "empty_timeout": 1000,
        "metadata": {
            "room_title": "Test room",
            "welcome_message": "Welcome to room",
            "room_features": {
            "allow_webcams": True,
            "mute_on_start": False,
            "allow_screen_share": True,
            "allow_rtmp": True,
            "admin_only_webcams": False,
            "allow_view_other_webcams": True,
            "allow_view_other_users_list": True,
            "allow_polls": True,
            "enable_analytics": True,
            "allow_virtual_bg": True,
            "allow_raise_hand": True,
            "auto_gen_user_id": False,
            "room_duration": 0,
            "recording_features": {
                "is_allow": True,
                "is_allow_cloud": True,
                "is_allow_local": True,
                "enable_auto_cloud_recording": False
            },
            "chat_features": {
                "allow_chat": True,
                "allow_file_upload": True
            },
            "shared_note_pad_features": {
                "allowed_shared_note_pad": True
            },
            "whiteboard_features": {
                "allowed_whiteboard": True
            },
            "external_media_player_features": {
                "allowed_external_media_player": True
            },
            "waiting_room_features": {
                "is_active": False
            },
            "breakout_room_features": {
                "is_allow": True,
                "allowed_number_rooms": 2
            },
            "display_external_link_features": {
                "is_allow": True
            },
            "ingress_features": {
                "is_allow": True
            },
            "speech_to_text_translation_features": {
                "is_allow": True,
                "is_allow_translation": True
            },
            "end_to_end_encryption_features": {
                "is_enabled": False
            }
            },
            "default_lock_settings": {
            "lock_microphone": False,
            "lock_webcam": False,
            "lock_screen_sharing": True,
            "lock_whiteboard": True,
            "lock_shared_notepad": True,
            "lock_chat": False,
            "lock_chat_send_message": False,
            "lock_chat_file_share": False,
            "lock_private_chat": False
            }
        }
    }
    status, result = await meet_platform.createRoom(data=CreateRoomRequest(**data))
    print(f"status: {status}")
    print(f"result: {result}")
    
if __name__ == "__main__":
    from asyncio import run
    run(main())