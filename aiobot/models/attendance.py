from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from aiobot.database import Base


class Attendance(Base):
    user_id = Column(String(50), ForeignKey('users.user_id'), nullable=False)
    time_in = Column(DateTime, default=datetime.utcnow)

    # user = relationship("User", back_populates="attendances")

    def __repr__(self):
        return f'<Attendance: user_id={self.user_id}, time_in={self.time_in}>'
