#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "ImportError: Django를 임포트 할 수 없습니다. 설치확인 및 환경변수를 확인하여 사용가능한지 확인해주세요"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
