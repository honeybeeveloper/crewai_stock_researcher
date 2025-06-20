from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

from nrclex import NRCLex # sentiment analysis lib



class SentimentAnalysisToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    text: str = Field(..., description="The text to analyze for emotions.")

class SentimentAnalysisTool(BaseTool):
    name: str = "MentionSentimentTool"
    description: str = (
        "Analyzes sentiment of a given piece of text and returns 'Joy', 'Sadness', 'Anger', 'Fear', 'Surprise', 'Disgust', 'Trust' and 'Anticipation'."
    )
    args_schema: Type[BaseModel] = SentimentAnalysisToolInput

    def _run(self, text: str) -> str:
        emotion = NRCLex(text)
        print(f">>> emotion.raw_emotion_scores : {emotion.raw_emotion_scores}")
        print(f">>> emotion.top_emotions : {emotion.top_emotions}")

        raw_scores = emotion.raw_emotion_scores
        sorted_scores = sorted(raw_scores.items(), key=lambda x: x[1], reverse=True)

        if not sorted_scores:
            return "No emotions detected in the input text."

        # result
        result_lines = ["🔍 Emotion Analysis Result:"]
        for emotion_name, score in sorted_scores:
            result_lines.append(f"- {emotion_name.capitalize()}: {score}")

        return "\n".join(result_lines)