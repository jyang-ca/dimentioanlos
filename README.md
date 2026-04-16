<div align="center">

<img width="1000" alt="banner_bordered_trimmed" src="https://github.com/user-attachments/assets/64f13b39-da06-4f58-add0-cfc44f04db4e" />

<h2>물리 공간을 위한 에이전트 네이티브 운영체제</h2>

[![Discord](https://img.shields.io/discord/1341146487186391173?style=flat-square&logo=discord&logoColor=white&label=Discord&color=5865F2)](https://discord.gg/dimos)
[![Stars](https://img.shields.io/github/stars/dimensionalOS/dimos?style=flat-square)](https://github.com/dimensionalOS/dimos/stargazers)
[![Forks](https://img.shields.io/github/forks/dimensionalOS/dimos?style=flat-square)](https://github.com/dimensionalOS/dimos/fork)
[![Contributors](https://img.shields.io/github/contributors/dimensionalOS/dimos?style=flat-square)](https://github.com/dimensionalOS/dimos/graphs/contributors)
![Nix](https://img.shields.io/badge/Nix-flakes-5277C3?style=flat-square&logo=NixOS&logoColor=white)
![NixOS](https://img.shields.io/badge/NixOS-supported-5277C3?style=flat-square&logo=NixOS&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-supported-76B900?style=flat-square&logo=nvidia&logoColor=white)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)

<a href="https://trendshift.io/repositories/23169" target="_blank"><img src="https://trendshift.io/api/badge/repositories/23169" alt="dimensionalOS%2Fdimos | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<big><big>

[하드웨어](#hardware) •
[설치](#installation) •
[에이전트 CLI 및 MCP](#agent-cli-and-mcp) •
[블루프린트](#blueprints) •
[개발](#development)

⚠️ **프리릴리스 베타** ⚠️

</big></big>

</div>

<a id="intro"></a>

# 소개

Dimensional은 범용 로보틱스를 위한 현대적인 운영체제입니다. 우리는 차세대 SDK 표준을 만들고 있으며, 대다수의 로봇 제조사와 통합되는 방향을 지향합니다.

간단한 설치만으로, ROS 없이도 휴머노이드, 사족보행 로봇, 드론에서 동작하는 물리 애플리케이션을 전부 Python으로 만들 수 있습니다.

Dimensional은 에이전트 네이티브입니다. 자연어로 로봇을 "바이브코딩"하고, 하드웨어와 자연스럽게 연결되는 로컬 및 호스팅 멀티에이전트 시스템을 구축할 수 있습니다. 에이전트는 네이티브 모듈로 실행되며, perception(라이다, 카메라)과 spatial memory부터 제어 루프와 모터 드라이버까지 내장 스트림을 구독합니다.
<table>
  <tr>
    <td align="center" width="50%">
      <a href="docs/capabilities/navigation/native/index.md"><img src="assets/readme/navigation.gif" alt="Navigation" width="100%"></a>
    </td>
    <td align="center" width="50%">
      <img src="assets/readme/perception.png" alt="Perception" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <h3><a href="docs/capabilities/navigation/native/index.md">내비게이션 및 매핑</a></h3>
      SLAM, 동적 장애물 회피, 경로 계획, 자율 탐색을 DimOS 네이티브와 ROS 양쪽으로 지원합니다.<br><a href="https://x.com/stash_pomichter/status/2010471593806545367">영상 보기</a>
    </td>
    <td align="center" width="50%">
      <h3>인지</h3>
      객체 탐지기, 3D 투영, VLM, 오디오 처리
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <a href="docs/capabilities/agents/readme.md"><img src="assets/readme/agentic_control.gif" alt="Agents" width="100%"></a>
    </td>
    <td align="center" width="50%">
      <img src="assets/readme/spatial_memory.gif" alt="Spatial Memory" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <h3><a href="docs/capabilities/agents/readme.md">에이전트 제어, MCP</a></h3>
      "로봇아, 주방을 찾아가"<br><a href="https://x.com/stash_pomichter/status/2015912688854200322">영상 보기</a>
    </td>
    <td align="center" width="50%">
      <h3>공간 메모리</h3>
      시공간 RAG, 동적 메모리, 객체 위치 추정과 지속성<br><a href="https://x.com/stash_pomichter/status/1980741077205414328">영상 보기</a>
    </td>
  </tr>
</table>


<a id="hardware"></a>

# 하드웨어

<table>
  <tr>
    <td align="center" width="20%">
      <h3>사족보행</h3>
      <img width="245" height="1" src="assets/readme/spacer.png">
    </td>
    <td align="center" width="20%">
      <h3>휴머노이드</h3>
      <img width="245" height="1" src="assets/readme/spacer.png">
    </td>
    <td align="center" width="20%">
      <h3>로봇 암</h3>
      <img width="245" height="1" src="assets/readme/spacer.png">
    </td>
    <td align="center" width="20%">
      <h3>드론</h3>
      <img width="245" height="1" src="assets/readme/spacer.png">
    </td>
    <td align="center" width="20%">
      <h3>기타</h3>
      <img width="245" height="1" src="assets/readme/spacer.png">
    </td>
  </tr>

  <tr>
    <td align="center" width="20%">
      🟩 <a href="docs/platforms/quadruped/go2/index.md">Unitree Go2 pro/air</a><br>
      🟥 <a href="dimos/robot/unitree/b1">Unitree B1</a><br>
    </td>
    <td align="center" width="20%">
      🟨 <a href="docs/platforms/humanoid/g1/index.md">Unitree G1</a><br>
    </td>
    <td align="center" width="20%">
      🟨 <a href="docs/capabilities/manipulation/readme.md">Xarm</a><br>
      🟨 <a href="docs/capabilities/manipulation/readme.md">AgileX Piper</a><br>
    </td>
    <td align="center" width="20%">
      🟧 <a href="dimos/robot/drone/README.md">MAVLink</a><br>
      🟧 <a href="dimos/robot/drone/README.md">DJI Mavic</a><br>
    </td>
    <td align="center" width="20%">
      🟥 <a href="https://github.com/dimensionalOS/openFT-sensor">힘/토크 센서</a><br>
    </td>
  </tr>
</table>
<br>
<div align="right">
🟩 안정화됨 🟨 베타 🟧 알파 🟥 실험적

</div>

> [!IMPORTANT]
> 🤖 OpenClaw, Claude Code 같은 선호하는 에이전트에 [AGENTS.md](AGENTS.md)와 [CLI 및 MCP](#agent-cli-and-mcp) 인터페이스를 알려 주면 강력한 Dimensional 애플리케이션을 바로 만들기 시작할 수 있습니다.

<a id="installation"></a>

# 설치

## 대화형 설치

```sh
curl -fsSL https://raw.githubusercontent.com/dimensionalOS/dimos/main/scripts/install.sh | bash
```

> 비대화형 설치와 고급 옵션은 [`scripts/install.sh --help`](scripts/install.sh)를 참고하세요.

## 수동 시스템 설치

시스템 의존성을 설정하려면 아래 가이드 중 하나를 따라가세요.

- 🟩 [Ubuntu 22.04 / 24.04](docs/installation/ubuntu.md)
- 🟩 [NixOS / 일반 Linux](docs/installation/nix.md)
- 🟧 [macOS](docs/installation/osx.md)

> 전체 시스템 요구사항, 검증된 구성, 의존성 티어는 [docs/requirements.md](docs/requirements.md)를 참고하세요.

## Python 설치

### 빠른 시작

```bash
uv venv --python "3.12"
source .venv/bin/activate
uv pip install 'dimos[base,unitree]'

# 기록된 사족보행 세션 재생(하드웨어 불필요)
# 참고: 첫 실행 시 LFS에서 약 75MB를 내려받는 동안 rerun 창이 검게 보일 수 있습니다
dimos --replay run unitree-go2
```

```bash
# 시뮬레이션 지원 포함 설치
uv pip install 'dimos[base,unitree,sim]'

# MuJoCo 시뮬레이션에서 사족보행 로봇 실행
dimos --simulation run unitree-go2

# 휴머노이드 시뮬레이션 실행
dimos --simulation run unitree-g1-sim
```

```bash
# 실제 로봇 제어(Unitree 사족보행 로봇, WebRTC 경유)
export ROBOT_IP=<YOUR_ROBOT_IP>
dimos run unitree-go2
```

# 주요 실행 예시

| 실행 명령 | 설명 |
|-------------|-------------|
| `dimos --replay run unitree-go2` | 사족보행 내비게이션 재생: SLAM, costmap, A* 경로 계획 |
| `dimos --replay --replay-dir unitree_go2_office_walk2 run unitree-go2-temporal-memory` | 사족보행 시간 메모리 재생 |
| `dimos --simulation run unitree-go2-agentic-mcp` | 시뮬레이션에서 사족보행 에이전트 + MCP 서버 실행 |
| `dimos --simulation run unitree-g1` | MuJoCo 시뮬레이션에서 휴머노이드 실행 |
| `dimos --replay run drone-basic` | 드론 영상 + 텔레메트리 재생 |
| `dimos --replay run drone-agentic` | 드론 + 비행 스킬을 갖춘 LLM 에이전트(재생) |
| `dimos run demo-camera` | 웹캠 데모, 하드웨어 불필요 |
| `dimos run keyboard-teleop-xarm7` | mock xArm7용 키보드 텔레옵(`dimos[manipulation]` extra 필요) |
| `dimos --simulation run unitree-go2-agentic-ollama` | 로컬 LLM 기반 사족보행 에이전트([Ollama](https://ollama.com) 및 `ollama serve` 필요) |

> 전체 블루프린트 문서는 [docs/usage/blueprints.md](docs/usage/blueprints.md)를 참고하세요.

<a id="agent-cli-and-mcp"></a>

# 에이전트 CLI 및 MCP

`dimos` CLI는 전체 라이프사이클을 관리합니다. 블루프린트 실행, 상태 확인, 에이전트와 상호작용, MCP를 통한 스킬 호출까지 모두 담당합니다.

```bash
dimos run unitree-go2-agentic-mcp --daemon   # 백그라운드에서 시작
dimos status                                 # 현재 실행 상태 확인
dimos log -f                                 # 로그 실시간 추적
dimos agent-send "explore the room"          # 에이전트에 명령 보내기
dimos mcp list-tools                         # 사용 가능한 MCP 스킬 목록
dimos mcp call relative_move --arg forward=0.5  # 스킬 직접 호출
dimos stop                                   # 종료
```

> 전체 CLI 레퍼런스는 [docs/usage/cli.md](docs/usage/cli.md)를 참고하세요.


# 사용법

## 라이브러리로서 DimOS 사용하기

아래는 로봇으로 연속적인 `cmd_vel` 스트림을 보내고 `color_image`를 단순 `Listener` 모듈로 전달받는 간단한 로봇 연결 모듈 예시입니다. DimOS 모듈은 표준화된 메시지를 사용해 서로 통신하는 로봇 내부 서브시스템입니다.

```py
import threading, time, numpy as np
from dimos.core.blueprints import autoconnect
from dimos.core.core import rpc
from dimos.core.module import Module
from dimos.core.stream import In, Out
from dimos.msgs.geometry_msgs import Twist
from dimos.msgs.sensor_msgs import Image, ImageFormat

class RobotConnection(Module):
    cmd_vel: In[Twist]
    color_image: Out[Image]

    @rpc
    def start(self):
        threading.Thread(target=self._image_loop, daemon=True).start()

    def _image_loop(self):
        while True:
            img = Image.from_numpy(
                np.zeros((120, 160, 3), np.uint8),
                format=ImageFormat.RGB,
                frame_id="camera_optical",
            )
            self.color_image.publish(img)
            time.sleep(0.2)

class Listener(Module):
    color_image: In[Image]

    @rpc
    def start(self):
        self.color_image.subscribe(lambda img: print(f"image {img.width}x{img.height}"))

if __name__ == "__main__":
    autoconnect(
        RobotConnection.blueprint(),
        Listener.blueprint(),
    ).build().loop()
```

<a id="blueprints"></a>

## 블루프린트

블루프린트는 모듈을 어떻게 구성하고 연결할지에 대한 명세입니다. 우리는 `autoconnect(...)`로 이를 조합하며, 이 함수는 `(name, type)` 기준으로 스트림을 연결하고 `Blueprint`를 반환합니다.

블루프린트는 조합 가능하고, 리매핑할 수 있으며, `autoconnect()`가 변수 이름 충돌이나 `In[]`/`Out[]` 메시지 타입 문제로 실패할 때 transport를 덮어쓸 수도 있습니다.

아래는 로봇의 이미지 스트림을 추론 및 행동 실행을 위한 LLM 에이전트에 연결하는 블루프린트 예시입니다.
```py
from dimos.core.blueprints import autoconnect
from dimos.core.transport import LCMTransport
from dimos.msgs.sensor_msgs import Image
from dimos.robot.unitree.go2.connection import go2_connection
from dimos.agents.agent import agent

blueprint = autoconnect(
    go2_connection(),
    agent(),
).transports({("color_image", Image): LCMTransport("/color_image", Image)})

# 블루프린트 실행
if __name__ == "__main__":
    blueprint.build().loop()
```

## 라이브러리 API

- [모듈](docs/usage/modules.md)
- [LCM](docs/usage/lcm.md)
- [블루프린트](docs/usage/blueprints.md)
- [트랜스포트](docs/usage/transports/index.md) — LCM, SHM, DDS, ROS 2
- [데이터 스트림](docs/usage/data_streams/README.md)
- [설정](docs/usage/configuration.md)
- [시각화](docs/usage/visualization.md)

## 데모

<img src="assets/readme/dimos_demo.gif" alt="DimOS Demo" width="100%">

<a id="development"></a>

# 개발

## DimOS에서 개발하기

```sh
export GIT_LFS_SKIP_SMUDGE=1
git clone -b dev https://github.com/dimensionalOS/dimos.git
cd dimos

uv sync --all-extras --no-extra dds

# 빠른 테스트 스위트 실행
uv run pytest dimos
```


## 다국어 지원

Python은 접착제이자 프로토타이핑 언어이지만, 우리는 LCM 상호운용성을 통해 여러 언어를 지원합니다.

언어 상호운용 예시는 아래를 확인하세요.
- [C++](examples/language-interop/cpp/)
- [Lua](examples/language-interop/lua/)
- [TypeScript](examples/language-interop/ts/)
