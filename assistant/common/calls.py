from typing import Dict, List, Optional, Union

import openai
from aiocache import cached
from openai.error import (
    APIConnectionError,
    APIError,
    RateLimitError,
    ServiceUnavailableError,
    Timeout,
)
from openai.version import VERSION
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)

from .constants import SUPPORTS_FUNCTIONS


@retry(
    retry=retry_if_exception_type(
        Union[
            Timeout,
            APIConnectionError,
            RateLimitError,
            ServiceUnavailableError,
        ]
    ),
    wait=wait_random_exponential(min=1, max=5),
    stop=stop_after_attempt(3),
    reraise=True,
)
@cached(ttl=1800)
async def request_embedding_raw(
    text: str,
    api_key: str,
    api_base: Optional[str] = None,
) -> List[float]:
    response = await openai.Embedding.acreate(
        input=text,
        model="text-embedding-ada-002",
        api_key=api_key,
        api_base=api_base,
        timeout=30,
    )
    return response["data"][0]["embedding"]


@retry(
    retry=retry_if_exception_type(
        Union[
            Timeout,
            APIConnectionError,
            RateLimitError,
            ServiceUnavailableError,
        ]
    ),
    wait=wait_random_exponential(min=1, max=5),
    stop=stop_after_attempt(3),
    reraise=True,
)
@cached(ttl=30)
async def request_chat_completion_raw(
    model: str,
    messages: List[dict],
    temperature: float,
    api_key: str,
    api_base: Optional[str] = None,
    functions: List[dict] = [],
    timeout: int = 60,
) -> Dict[str, str]:
    if functions and VERSION >= "0.27.6" and model in SUPPORTS_FUNCTIONS:
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            temperature=temperature,
            api_key=api_key,
            api_base=api_base,
            functions=functions,
            timeout=timeout,
        )
    else:
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            temperature=temperature,
            api_key=api_key,
            api_base=api_base,
            timeout=timeout,
        )
    return response["choices"][0]["message"]


@retry(
    retry=retry_if_exception_type(
        Union[
            Timeout,
            APIConnectionError,
            RateLimitError,
            APIError,
            ServiceUnavailableError,
        ]
    ),
    wait=wait_random_exponential(min=1, max=5),
    stop=stop_after_attempt(3),
    reraise=True,
)
@cached(ttl=30)
async def request_completion_raw(
    model: str,
    prompt: str,
    temperature: float,
    api_key: str,
    api_base: Optional[str] = None,
    max_tokens: int = 250,
    timeout: int = 60,
) -> str:
    response = await openai.Completion.acreate(
        model=model,
        prompt=prompt,
        temperature=temperature,
        api_key=api_key,
        api_base=api_base,
        max_tokens=max_tokens,
        timeout=timeout,
    )
    return response["choices"][0]["text"]