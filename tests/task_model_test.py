from datetime import datetime

from npg_porch.models.task import TaskExpanded, TaskStateEnum
from npg_porch.models.event import LatestEvent
from npg_porch.models import Pipeline


def test_expanded_task_date_format():
    pipeline = Pipeline(
        name="pipeline", version="1.0", uri="file:///team117/test_pipeline"
    )
    task = TaskExpanded(
        task_id=1,
        pipeline=pipeline,
        created=datetime(2025, 1, 1, 0, 0, 0),
        latest_event=LatestEvent(
            task_id=1, status_date=datetime(2025, 1, 2, 12, 30, 15)
        ),
        status=TaskStateEnum.PENDING,
    )
    assert str(task.created) == "2025-01-01 00:00:00"
    assert str(task.latest_event.status_date) == "2025-01-02 12:30:15"
