from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from chatbot.application.service.command.send_message_service import SendMessageService
from chatbot.application.service.query.get_conversation_service import GetConversationService
from chatbot.domain.model.message import Message, Response
from chatbot.infrastructure.repository.message_repository import MessageRepository
from chatbot.infrastructure.publisher.event_publisher import EventPublisher

router = APIRouter()

# Request y Response
class SendMessageRequest(BaseModel):
    user_id: str
    message_text: str

class MessageResponse(BaseModel):
    message_text: str
    response_text: str

# Dependencias (repositorios y publicadores)
message_repo = MessageRepository()
event_publisher = EventPublisher()
send_message_service = SendMessageService(message_repo=message_repo, event_publisher=event_publisher)
get_conversation_service = GetConversationService(message_repo=message_repo)

@router.post("/chat/send", response_model=MessageResponse)
async def send_message(request: SendMessageRequest):
    try:
        response: Response = send_message_service.send_message(request.user_id, request.message_text)
        return MessageResponse(
            message_text=request.message_text,
            response_text=response.text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/chat/history/{user_id}", response_model=List[MessageResponse])
async def get_conversation(user_id: str):
    try:
        conversation: List[Message] = get_conversation_service.get_conversation(user_id)
        response_list = [
            MessageResponse(
                message_text=msg.text,
                response_text=msg.response.text if hasattr(msg, "response") and msg.response else ""
            )
            for msg in conversation
        ]
        return response_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
