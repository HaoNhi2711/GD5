# # chuẩn bị dữ liệu
from ingestion.ingestion import Ingestion

Ingestion("openai").ingestion_folder(
     path_input_folder="demo\data_in",
     path_vector_store="demo\data_vector",
)

# chatbot
from chatbot.services.files_chat_agent import FilesChatAgent  # noqa: E402
from app.config import settings

settings.LLM_NAME = "openai"

_question = "Triệu chứng bệnh tim?"
chat = FilesChatAgent("D:\ChatBotThucTap\demo\data_vector").get_workflow().compile().invoke(
    input={
        "question": _question,
    }
)

print(chat)

print("generation", chat["generation"])