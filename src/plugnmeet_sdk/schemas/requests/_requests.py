from typing import List, Optional
from attrs import define, field
from ..data._data import RoomMetadata, UserInfo, OrderBy

@define
class CreateRoomRequest:
    room_id: str
    max_participants: Optional[int] = None
    empty_timeout: Optional[int] = None
    metadata: RoomMetadata
    
@define
class GetActiveRoomInfoRequest:
    room_id: str

@define
class GetActiveRoomsInfoRequest:
    pass

@define
class RoomStatusRequest:
    room_id: str
    
@define
class JoinRoomRequest:
    room_id: str
    user_info: UserInfo
    
@define
class FetchPastRoomsInfoRequest:
    room_ids: List[str]
    from_: Optional[int] = field(default=None, alias='from')
    limit: Optional[int] = None
    order_by: Optional[OrderBy] = None

@define
class EndRoomRequest:
    room_id: str

@define
class FetchAnalyticsRequest:
    room_ids: List[str]
    from_: Optional[int] = field(default=None, alias='from')
    limit: Optional[int] = None
    order_by: Optional[OrderBy] = None
    
@define
class DeleteAnalyticsRequest:
    file_id: str
    
@define
class GetAnalyticsDownloadTokenRequest:
    file_id: str
    
@define
class FetchRecordingsRequest:
    room_ids: List[str]
    from_: Optional[int] = field(default=None, alias='from')
    limit: Optional[int] = None
    order_by: Optional[OrderBy] = None
    
@define
class RecordingInfoRequest:
    record_id: str
    
@define
class DeleteRecordingsRequest:
    record_id: str
    
@define
class GetRecordingDownloadTokenRequest:
    record_id: str
    
@define
class GetClientFilesRequest:
    pass
