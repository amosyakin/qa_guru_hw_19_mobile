from pathlib import Path

import qu_guru_hw_19_mobile


def abs_path_from_project(relative_path: str):
    return (
        Path(qu_guru_hw_19_mobile.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
