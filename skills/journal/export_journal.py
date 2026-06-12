"""Journal export skill."""

from typing import List, Dict
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def export_to_csv(entries: List[Dict[str, object]]) -> str:
    if not entries:
        return ""

    headers = list(entries[0].keys())
    lines = [",".join(headers)]
    for entry in entries:
        lines.append(",".join(str(entry.get(header, "")) for header in headers))
    return "\n".join(lines)

METADATA = SkillMetadata(
    name='skills.journal.export_journal',
    description='Export journal entries to CSV format.',
    version='1.0.0',
    category='journal',
    inputs=[
        SkillIO(name='entries', description='Journal entries to export.', data_type='List[Dict[str, object]]', required=True, example=[{'symbol': 'EURUSD', 'profit': 10.0}]),
    ],
    outputs=[
        SkillIO(name='csv_text', description='CSV-formatted string of journal entries.', data_type='str', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'entries': [{'symbol': 'EURUSD', 'profit': 10.0}]}, 'output': 'symbol,profit\\nEURUSD,10.0'}],
    tags=['journal', 'export'],
)
