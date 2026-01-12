from enum import Enum

class UserEvent(Enum):
    PLAY = "play"
    PAUSE = "pause"
    RESUME = "resume"
    SKIP = "skip"
    ASK_QUESTION = "ask_question"
    END_QA = "end_qa"
