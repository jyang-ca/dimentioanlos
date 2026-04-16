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

import importlib


def test_build_openai_client_kwargs_reads_proxy_env(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:8080/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "pwd")

    from dimos.utils.openai_client import build_openai_client_kwargs

    assert build_openai_client_kwargs() == {
        "api_key": "pwd",
        "base_url": "http://127.0.0.1:8080/v1",
    }


def test_openai_vl_model_uses_proxy_env(monkeypatch) -> None:
    calls: list[dict[str, str]] = []

    class FakeOpenAI:
        def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
            calls.append(kwargs)

    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:8080/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "pwd")

    module = importlib.import_module("dimos.models.vl.openai")
    monkeypatch.setattr(module, "OpenAI", FakeOpenAI)

    model = module.OpenAIVlModel()
    _ = model._client

    assert calls == [{"api_key": "pwd", "base_url": "http://127.0.0.1:8080/v1"}]


def test_openai_tts_node_uses_proxy_env(monkeypatch) -> None:
    calls: list[dict[str, str]] = []

    class FakeOpenAI:
        def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
            calls.append(kwargs)

    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:8080/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "pwd")

    module = importlib.import_module("dimos.stream.audio.tts.node_openai")
    monkeypatch.setattr(module, "OpenAI", FakeOpenAI)

    _ = module.OpenAITTSNode()

    assert calls == [{"api_key": "pwd", "base_url": "http://127.0.0.1:8080/v1"}]


def test_unitree_speak_uses_proxy_env(monkeypatch) -> None:
    calls: list[dict[str, str]] = []

    class FakeOpenAI:
        def __init__(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
            calls.append(kwargs)

    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:8080/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "pwd")

    module = importlib.import_module("dimos.skills.unitree.unitree_speak")
    monkeypatch.setattr(module, "OpenAI", FakeOpenAI)

    skill = module.UnitreeSpeak(text="hello")
    _ = skill._get_openai_client()

    assert calls == [{"api_key": "pwd", "base_url": "http://127.0.0.1:8080/v1"}]
