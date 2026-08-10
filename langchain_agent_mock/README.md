# LangChain Agent Mock

LangChain의 `@tool`과 `invoke()` 흐름만 연습하는 최소 목업 프로젝트입니다.
실제 LLM이나 API 키 없이 실행됩니다.

## 실행

```powershell
cd langchain_agent_mock
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python agent_demo.py
```

예상 결과:

```text
도구 호출 결과: 5
```

다음 실습에서는 `run_agent()`의 라우터를 실제 LLM 기반 LangChain agent로 교체하면 됩니다.
