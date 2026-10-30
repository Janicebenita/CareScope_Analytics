"""Review fictional CareScope capacity indicators for an operations user."""
from __future__ import annotations


def review_capacity(snapshot: dict) -> dict:
    occupied = max(int(snapshot.get("occupied_beds", 0)), 0)
    beds = max(int(snapshot.get("total_beds", 0)), 0)
    wait = max(float(snapshot.get("average_wait_minutes", 0)), 0)
    staff_gap = max(int(snapshot.get("unfilled_shifts", 0)), 0)
    occupancy = round(occupied / beds, 3) if beds else None
    flags = []
    if occupancy is None:
        flags.append("missing-bed-capacity")
    elif occupancy >= 0.9:
        flags.append("high-simulated-occupancy")
    if wait >= 60:
        flags.append("long-simulated-wait")
    if staff_gap:
        flags.append("unfilled-simulated-shifts")
    return {"occupancy_rate": occupancy, "flags": flags, "evidence": {"occupied_beds": occupied, "total_beds": beds, "average_wait_minutes": wait, "unfilled_shifts": staff_gap}, "data_status": "fictional-demonstration", "clinical_use_prohibited": True, "human_review_required": True}
