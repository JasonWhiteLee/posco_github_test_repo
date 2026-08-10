"""가장 작은 형태의 LangGraph 상태 그래프 예제."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GreetingState(TypedDict):
    name: str
    message: str


def prepare_name(state: GreetingState) -> dict[str, str]:
    """이름이 비어 있으면 기본 이름을 사용한다."""
    return {"name": state.get("name", "").strip() or "LangGraph"}


def create_greeting(state: GreetingState) -> dict[str, str]:
    """상태의 이름으로 인사말을 만든다."""
    return {"message": f"안녕하세요, {state['name']}!"}


def build_graph():
    graph = StateGraph(GreetingState)
    graph.add_node("prepare_name", prepare_name)
    graph.add_node("create_greeting", create_greeting)
    graph.add_edge(START, "prepare_name")
    graph.add_edge("prepare_name", "create_greeting")
    graph.add_edge("create_greeting", END)
    return graph.compile()


if __name__ == "__main__":
    result = build_graph().invoke({"name": "LangGraph", "message": ""})
    print(result["message"])
