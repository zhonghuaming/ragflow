#
#  Copyright 2024 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  AFTER UPDATING THIS FILE, PLEASE ENSURE THAT docs/references/supported_models.mdx IS ALSO UPDATED for consistency!
#
from .embedding_model import (
    OllamaEmbed,
    LocalAIEmbed,
    OpenAIEmbed,
    AzureEmbed,
    XinferenceEmbed,
    QWenEmbed,
    ZhipuEmbed,
    FastEmbed,
    YoudaoEmbed,
    BaiChuanEmbed,
    JinaEmbed,
    DefaultEmbedding,
    MistralEmbed,
    BedrockEmbed,
    GeminiEmbed,
    NvidiaEmbed,
    LmStudioEmbed,
    OpenAI_APIEmbed,
    CoHereEmbed,
    TogetherAIEmbed,
    PerfXCloudEmbed,
    UpstageEmbed,
    SILICONFLOWEmbed,
    ReplicateEmbed,
    BaiduYiyanEmbed,
    VoyageEmbed,
    HuggingFaceEmbed,
    VolcEngineEmbed,
    GPUStackEmbed,
)
from .chat_model import (
    GptTurbo,
    AzureChat,
    ZhipuChat,
    QWenChat,
    OllamaChat,
    LocalAIChat,
    XinferenceChat,
    MoonshotChat,
    DeepSeekChat,
    VolcEngineChat,
    BaiChuanChat,
    MiniMaxChat,
    MistralChat,
    GeminiChat,
    BedrockChat,
    GroqChat,
    OpenRouterChat,
    StepFunChat,
    NvidiaChat,
    LmStudioChat,
    OpenAI_APIChat,
    CoHereChat,
    LeptonAIChat,
    TogetherAIChat,
    PerfXCloudChat,
    UpstageChat,
    NovitaAIChat,
    SILICONFLOWChat,
    PPIOChat,
    YiChat,
    ReplicateChat,
    HunyuanChat,
    SparkChat,
    BaiduYiyanChat,
    AnthropicChat,
    GoogleChat,
    HuggingFaceChat,
    GPUStackChat,
    ModelScopeChat,
)

from .cv_model import (
    GptV4,
    AzureGptV4,
    OllamaCV,
    XinferenceCV,
    QWenCV,
    Zhipu4V,
    LocalCV,
    GeminiCV,
    OpenRouterCV,
    LocalAICV,
    NvidiaCV,
    LmStudioCV,
    StepFunCV,
    OpenAI_APICV,
    TogetherAICV,
    YiCV,
    HunyuanCV,
)
from .rerank_model import (
    LocalAIRerank,
    DefaultRerank,
    JinaRerank,
    YoudaoRerank,
    XInferenceRerank,
    NvidiaRerank,
    LmStudioRerank,
    OpenAI_APIRerank,
    CoHereRerank,
    TogetherAIRerank,
    SILICONFLOWRerank,
    BaiduYiyanRerank,
    VoyageRerank,
    QWenRerank,
    GPUStackRerank,
)
from .sequence2txt_model import (
    GPTSeq2txt,
    QWenSeq2txt,
    AzureSeq2txt,
    XinferenceSeq2txt,
    TencentCloudSeq2txt,
    GPUStackSeq2txt,
)
from .tts_model import (
    FishAudioTTS,
    QwenTTS,
    OpenAITTS,
    SparkTTS,
    XinferenceTTS,
    GPUStackTTS,
)

EmbeddingModel = {
    "Ollama": OllamaEmbed,
    "LocalAI": LocalAIEmbed,
    "OpenAI": OpenAIEmbed,
    "Azure-OpenAI": AzureEmbed,
    "Xinference": XinferenceEmbed,
    "Tongyi-Qianwen": QWenEmbed,
    "ZHIPU-AI": ZhipuEmbed,
    "FastEmbed": FastEmbed,
    "Youdao": YoudaoEmbed,
    "BaiChuan": BaiChuanEmbed,
    "Jina": JinaEmbed,
    "BAAI": DefaultEmbedding,
    "Mistral": MistralEmbed,
    "Bedrock": BedrockEmbed,
    "Gemini": GeminiEmbed,
    "NVIDIA": NvidiaEmbed,
    "LM-Studio": LmStudioEmbed,
    "OpenAI-API-Compatible": OpenAI_APIEmbed,
    "VLLM": OpenAI_APIEmbed,
    "Cohere": CoHereEmbed,
    "TogetherAI": TogetherAIEmbed,
    "PerfXCloud": PerfXCloudEmbed,
    "Upstage": UpstageEmbed,
    "SILICONFLOW": SILICONFLOWEmbed,
    "Replicate": ReplicateEmbed,
    "BaiduYiyan": BaiduYiyanEmbed,
    "Voyage AI": VoyageEmbed,
    "HuggingFace": HuggingFaceEmbed,
    "VolcEngine": VolcEngineEmbed,
    "GPUStack": GPUStackEmbed,
}

CvModel = {
    "OpenAI": GptV4,
    "Azure-OpenAI": AzureGptV4,
    "Ollama": OllamaCV,
    "Xinference": XinferenceCV,
    "Tongyi-Qianwen": QWenCV,
    "ZHIPU-AI": Zhipu4V,
    "Moonshot": LocalCV,
    "Gemini": GeminiCV,
    "OpenRouter": OpenRouterCV,
    "LocalAI": LocalAICV,
    "NVIDIA": NvidiaCV,
    "LM-Studio": LmStudioCV,
    "StepFun": StepFunCV,
    "OpenAI-API-Compatible": OpenAI_APICV,
    "VLLM": OpenAI_APICV,
    "TogetherAI": TogetherAICV,
    "01.AI": YiCV,
    "Tencent Hunyuan": HunyuanCV,
}

ChatModel = {
    "OpenAI": GptTurbo,
    "Azure-OpenAI": AzureChat,
    "ZHIPU-AI": ZhipuChat,
    "Tongyi-Qianwen": QWenChat,
    "Ollama": OllamaChat,
    "LocalAI": LocalAIChat,
    "Xinference": XinferenceChat,
    "Moonshot": MoonshotChat,
    "DeepSeek": DeepSeekChat,
    "VolcEngine": VolcEngineChat,
    "BaiChuan": BaiChuanChat,
    "MiniMax": MiniMaxChat,
    "Mistral": MistralChat,
    "Gemini": GeminiChat,
    "Bedrock": BedrockChat,
    "Groq": GroqChat,
    "OpenRouter": OpenRouterChat,
    "StepFun": StepFunChat,
    "NVIDIA": NvidiaChat,
    "LM-Studio": LmStudioChat,
    "OpenAI-API-Compatible": OpenAI_APIChat,
    "VLLM": OpenAI_APIChat,
    "Cohere": CoHereChat,
    "LeptonAI": LeptonAIChat,
    "TogetherAI": TogetherAIChat,
    "PerfXCloud": PerfXCloudChat,
    "Upstage": UpstageChat,
    "novita.ai": NovitaAIChat,
    "SILICONFLOW": SILICONFLOWChat,
    "PPIO": PPIOChat,
    "01.AI": YiChat,
    "Replicate": ReplicateChat,
    "Tencent Hunyuan": HunyuanChat,
    "XunFei Spark": SparkChat,
    "BaiduYiyan": BaiduYiyanChat,
    "Anthropic": AnthropicChat,
    "Google Cloud": GoogleChat,
    "HuggingFace": HuggingFaceChat,
    "GPUStack": GPUStackChat,
    "ModelScope":ModelScopeChat,
}

RerankModel = {
    "LocalAI": LocalAIRerank,
    "BAAI": DefaultRerank,
    "Jina": JinaRerank,
    "Youdao": YoudaoRerank,
    "Xinference": XInferenceRerank,
    "NVIDIA": NvidiaRerank,
    "LM-Studio": LmStudioRerank,
    "OpenAI-API-Compatible": OpenAI_APIRerank,
    "VLLM": CoHereRerank,
    "Cohere": CoHereRerank,
    "TogetherAI": TogetherAIRerank,
    "SILICONFLOW": SILICONFLOWRerank,
    "BaiduYiyan": BaiduYiyanRerank,
    "Voyage AI": VoyageRerank,
    "Tongyi-Qianwen": QWenRerank,
    "GPUStack": GPUStackRerank,
}

Seq2txtModel = {
    "OpenAI": GPTSeq2txt,
    "Tongyi-Qianwen": QWenSeq2txt,
    "Azure-OpenAI": AzureSeq2txt,
    "Xinference": XinferenceSeq2txt,
    "Tencent Cloud": TencentCloudSeq2txt,
    "GPUStack": GPUStackSeq2txt,
}

TTSModel = {
    "Fish Audio": FishAudioTTS,
    "Tongyi-Qianwen": QwenTTS,
    "OpenAI": OpenAITTS,
    "XunFei Spark": SparkTTS,
    "Xinference": XinferenceTTS,
    "GPUStack": GPUStackTTS,
}
