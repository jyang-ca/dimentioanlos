# Copyright 2025-2026 Dimensional Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os


def build_openai_client_kwargs(
    api_key: str | None = None,
    base_url: str | None = None,
) -> dict[str, str]:
    """Build OpenAI client kwargs from explicit args or environment variables."""
    client_kwargs: dict[str, str] = {}

    resolved_api_key = api_key or os.getenv("OPENAI_API_KEY")
    resolved_base_url = base_url or os.getenv("OPENAI_BASE_URL")

    if resolved_api_key:
        client_kwargs["api_key"] = resolved_api_key
    if resolved_base_url:
        client_kwargs["base_url"] = resolved_base_url

    return client_kwargs
