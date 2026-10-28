# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2026 Novikov Laboratories LLC
# Commercial licenses for use outside the AGPL: see COMMERCIAL.md
"""Smoke test of an installed sequentialist-core: `python tools/smoke_test.py VERSION`, outside the checkout.

Checks that the installed package is the expected version, that the
`sequentialist` namespace stays open to the other libraries, that its
commands are registered, and that a task runs, survives being reopened
and keeps a verifiable audit log.
"""
import sys
from importlib.metadata import entry_points, version


def main(expected: str) -> int:
    from sequential_analysis.procedures import MeanEDetector

    import sequentialist
    import sequentialist.core as core

    assert core.__version__ == expected == version("sequentialist-core"), (core.__version__, expected)
    assert getattr(sequentialist, "__file__", None) is None, "the sequentialist namespace must stay open"
    found = entry_points()
    commands = found.select(group="sequentialist.commands") if hasattr(found, "select") else \
        found.get("sequentialist.commands", [])
    assert {"audit", "tasks"} <= {p.name for p in commands}

    class Watch(core.Handler):
        def streams(self):
            return {"mean": core.Stream(MeanEDetector(m=0.2, arl=100, direction="increase"))}

        def on_record(self, record, ctx):
            event = ctx.step("mean", {"x": record.data["x"]})
            if event is not None and event.terminal:
                ctx.record("decision", "alarm", evidence=["mean"])
                ctx.restart("mean", "alarm")

    engine = core.Engine(core.MemoryStorage(), clock="event")
    task = engine.create("smoke", "smoke.watch/1", {}, Watch())
    task.ingest([core.Record("s", i, {"x": 0.1 if i < 100 else 0.9}, float(i)) for i in range(300)])
    task.close()
    task = engine.open("smoke", lambda spec: Watch())
    entries = [e.to_json() for e in task.audit()]
    task.close()
    assert core.verify_audit(entries, "smoke") == len(entries)
    assert any(e["decision"] == "alarm" for e in entries)
    print(f"sequentialist-core {expected}: installed, task run and reopened, {len(entries)} audit entries verified")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
