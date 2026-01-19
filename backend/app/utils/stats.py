from datetime import datetime

class BotStats:
    def __init__(self):
        self.start_time = datetime.utcnow()
        self.total_updates = 0
        self.unique_users = set()
        self.last_activity = None

    def register_update(self, user_id: int | None):
        self.total_updates += 1
        self.last_activity = datetime.utcnow()
        if user_id:
            self.unique_users.add(user_id)

    def snapshot(self) -> dict:
        uptime = datetime.utcnow() - self.start_time
        return {
            "uptime_minutes": round(uptime.total_seconds() / 60, 2),
            "total_updates": self.total_updates,
            "unique_users": len(self.unique_users),
            "last_activity": self.last_activity.isoformat() if self.last_activity else None,
        }