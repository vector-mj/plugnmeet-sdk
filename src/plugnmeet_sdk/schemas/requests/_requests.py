from typing import List, Optional
from dataclasses import dataclass, field
from ..data._data import RoomMetadata, UserInfo, OrderBy

@dataclass
class CreateRoomRequest:
    room_id: str
    metadata: RoomMetadata
    max_participants: Optional[int] = None
    empty_timeout: Optional[int] = None
    
@dataclass
class GetActiveRoomInfoRequest:
    room_id: str

@dataclass
class GetActiveRoomsInfoRequest:
    pass

@dataclass
class RoomStatusRequest:
    room_id: str
    
@dataclass
class JoinRoomRequest:
    room_id: str
    user_info: UserInfo
    
@dataclass
class FetchPastRoomsInfoRequest:
    room_ids: List[str]
    from_: Optional[int] = field(default=None)
    limit: Optional[int] = None
    order_by: Optional[OrderBy] = None

@dataclass
class EndRoomRequest:
    room_id: str

@dataclass
class FetchAnalyticsRequest:
    room_ids: List[str]
    from_: Optional[int] = field(default=None)
    limit: Optional[int] = None
    order_by: Optional[OrderBy] = None
    
@dataclass
class DeleteAnalyticsRequest:
    file_id: str
    
@dataclass
class GetAnalyticsDownloadTokenRequest:
    file_id: str
    
@dataclass
class FetchRecordingsRequest:
    room_ids: List[str]
    from_: Optional[int] = field(default=None)
    limit: Optional[int] = None
    order_by: Optional[OrderBy] = None
    
@dataclass
class RecordingInfoRequest:
    record_id: str
    
@dataclass
class DeleteRecordingsRequest:
    record_id: str
    
@dataclass
class GetRecordingDownloadTokenRequest:
    record_id: str
    
@dataclass
class GetClientFilesRequest:
    pass
