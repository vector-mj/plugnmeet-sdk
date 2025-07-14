from typing import Dict, Optional, Tuple
from aiohttp import ClientSession
from .utils import generate_hmac
from json import dumps
from .schemas.requests import *
from dataclasses import asdict
from .exceptions import RequestErrorException

class PlugNMeet:
    def __init__(self, base_url:str, api_key:str, api_secret: str):
        self._base_url = base_url + "/auth"
        self._api_key = api_key
        self._api_secret = api_secret
    
    def _generate_header(self, body: str):
        headers =  {
            "Content-Type": "application/json",
            "API-KEY": self._api_key,
            "HASH-SIGNATURE": generate_hmac(message=body, secret=self._api_secret)
        }
        return headers
        
    async def _async_request(self, path:str, data: Optional[dict] = {}):
        try:
            url = self._base_url + path
            headers = self._generate_header(body=dumps(data))
            async with ClientSession(headers=headers) as session:
                async with session.post(url=url, json=data) as response:
                    print(response.content_type)
                    return response.status, await response.json()
        except Exception as e:
            raise RequestErrorException from e
        
    async def createRoom(self, data: CreateRoomRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/room/create", data=asdict(data))
    
    async def getJoinToken(self, data: JoinRoomRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/room/getJoinToken", data=asdict(data))
    
    async def isRoomActive(self, data: RoomStatusRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/room/isRoomActive", data=asdict(data))
        
    async def getActiveRoomInfo(self, data: GetActiveRoomInfoRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/room/getActiveRoomInfo", data=asdict(data))
        
    async def getActiveRoomsInfo(self)->Tuple[int,Dict]:
        return await self._async_request(path="/room/getActiveRoomsInfo", data=dict({}))

    async def fetchPastRoomsInfo(self, data=FetchPastRoomsInfoRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/room/fetchPastRooms", data=asdict(data))
    
    async def endRoom(self, data=EndRoomRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/room/endRoom", data=asdict(data))
    
    async def fetchAnalytics(self, data: FetchAnalyticsRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/analytics/fetch", data=asdict(data))

    async def deleteAnalytics(self, data: DeleteAnalyticsRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/analytics/delete", data=asdict(data))

    async def getAnalyticsDownloadToken(self, data: GetAnalyticsDownloadTokenRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/analytics/getDownloadToken", data=asdict(data))

    async def fetchRecordings(self, data: FetchRecordingsRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/recording/fetch", data=asdict(data))

    async def recordingInfo(self, data: RecordingInfoRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/recording/recordingInfo", data=asdict(data))
    
    async def deleteRecordings(self, data: DeleteRecordingsRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/recording/delete", data=asdict(data))

    async def getRecordingDownloadToken(self, data: GetRecordingDownloadTokenRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/recording/getDownloadToken", data=asdict(data))

    async def getClientFiles(self, data: GetClientFilesRequest)->Tuple[int,Dict]:
        return await self._async_request(path="/getClientFiles", data=asdict(data))
