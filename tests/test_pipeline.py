from src.core.pipeline import Pipeline


class _Stage:
    def __init__(self, name):
        self.name = name
        self.seen = []

    def process(self, ctx):
        self.seen.append(ctx["tick"])
        ctx.setdefault("trace", []).append(self.name)
        return ctx


def test_pipeline_stage_order():
    a, b, c = _Stage("a"), _Stage("b"), _Stage("c")
    pipe = Pipeline(handlers=[a], processors=[b], drivers=[c])
    ctx = {"handle": None, "tick": 0}
    for stage in (*pipe.handlers, *pipe.processors, *pipe.drivers):
        ctx = stage.process(ctx)
    assert ctx["trace"] == ["a", "b", "c"]