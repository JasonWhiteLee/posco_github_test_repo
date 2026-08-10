"""아주 작은 LangChain 도구 호출 목업."""

from langchain_core.tools import tool


@tool
def add_numbers(a: int, b: int) -> int:
    """두 수를 더한다."""
    return a + b


def run_agent(question: str) -> str:
    """실습용 라우터: 질문을 보고 도구를 호출한다."""
    if "더" in question or "+" in question:
        result = add_numbers.invoke({"a": 2, "b": 3})
        return f"도구 호출 결과: {result}"
    return "목업 에이전트: 아직 연결된 도구가 없습니다."


if __name__ == "__main__":
    print(run_agent("2와 3을 더해줘"))
