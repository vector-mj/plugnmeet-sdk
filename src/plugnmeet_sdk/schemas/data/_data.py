from typing import Optional
from attrs import define
from enum import Enum

class OrderBy(str,Enum):
    DESC="DESC"
    ASC="ASC"

@define
class RecordingFeatures:
    is_allow: bool
    is_allow_cloud: bool
    is_allow_local: bool
    enable_auto_cloud_recording: bool
    
@define
class ChatFeatures:
    allow_chat:	bool
    allow_file_upload: bool
    
@define
class SharedNotePadFeatures:	
    allowed_shared_note_pad: bool
    
@define
class WhiteboardFeatures:	
    allowed_whiteboard:	bool
    preload_file: Optional[str] = None
    
@define
class ExternalMediaPlayerFeatures:
    allowed_external_media_player:	bool
    
@define
class WaitingRoomFeatures:	
    is_active: bool
    
@define
class BreakoutRoomFeatures:
    is_allow: bool
    allowed_number_rooms: int
    
@define
class DisplayExternalLinkFeatures:
    is_allow: bool

@define
class IngressFeatures:
    is_allow: bool
    
@define
class SpeechToTextTranslationFeatures:
    is_allow: bool
    
@define
class EndToEndEncryptionFeatures:
    is_enabled: bool
    included_chat_messages: bool
    included_whiteboard: bool
    
@define
class RoomFeatures:
    allow_webcams: bool    
    mute_on_start: bool  
    allow_screen_share: bool
    allow_rtmp: bool
    admin_only_webcams: bool
    allow_view_other_webcams: bool
    allow_view_other_users_list: bool
    enable_analytics: Optional[bool] = None
    allow_virtual_bg: Optional[bool] = None
    allow_raise_hand: Optional[bool] = None
    auto_gen_user_id: Optional[bool] = None
    room_duration: Optional[int] = None
    recording_features: RecordingFeatures
    chat_features: ChatFeatures
    shared_note_pad_features: SharedNotePadFeatures	
    whiteboard_features: WhiteboardFeatures
    external_media_player_features: ExternalMediaPlayerFeatures
    waiting_room_features: WaitingRoomFeatures
    breakout_room_features: BreakoutRoomFeatures
    display_external_link_features: DisplayExternalLinkFeatures
    ingress_features: Optional[IngressFeatures] = None
    speech_to_text_translation_features: Optional[SpeechToTextTranslationFeatures] = None
    end_to_end_encryption_features: Optional[EndToEndEncryptionFeatures] = None

@define
class DefaultLockSettings:
    lock_microphone: Optional[bool] = None
    lock_webcam: Optional[bool] = None
    lock_screen_sharing: Optional[bool] = None
    lock_chat: Optional[bool] = None
    lock_chat_send_message: Optional[bool] = None
    lock_chat_file_share: Optional[bool] = None

@define
class CopyrightConf:
    display: bool
    text: str

@define
class RoomMetadata:
    room_title: str
    welcome_message: Optional[str] = None
    webhook_url: Optional[str] = None
    logout_url: Optional[str] = None
    room_features: RoomFeatures
    default_lock_settings: Optional[DefaultLockSettings] = None
    copyright_conf: Optional[CopyrightConf] = None
    extra_data: Optional[str] = None
    
@define
class  UserMetadata:
    profile_pic: Optional[str] = None
    preferred_lang: Optional[str] = None
    record_webcam: Optional[bool] = None
    ex_user_id: Optional[str] = None
    extra_data: Optional[str] = None
    lock_settings: Optional[DefaultLockSettings] = None
    
@define
class UserInfo:
    name: str
    user_id: str
    is_admin: bool
    is_hidden: Optional[bool] = None
    user_metadata: UserMetadata
    
__all__ = (
    "OrderBy",
    "RecordingFeatures",
    "ChatFeatures",
    "SharedNotePadFeatures",
    "WhiteboardFeatures",
    "ExternalMediaPlayerFeatures",
    "WaitingRoomFeatures",
    "BreakoutRoomFeatures",
    "DisplayExternalLinkFeatures",
    "IngressFeatures",
    "SpeechToTextTranslationFeatures",
    "EndToEndEncryptionFeatures",
    "RoomFeatures",
    "DefaultLockSettings",
    "CopyrightConf",
    "RoomMetadata",
    "UserMetadata",
    "UserInfo"
)