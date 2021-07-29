from setup import db

class TeamModel(db.Model):
    __tablename__ = 'teams'
    __bind_key__ = 'teams'
    team_id = db.Column(db.Integer(), primary_key=True)
    team_name = db.Column(db.String(255), nullable=False)
    teams = db.relationship('MemberModel', backref='teams')

    def __repr__(self) -> str:
        return (
            f"**Team** "
            f"team_id: {self.team_id} "
            f"team_name: {self.team_name} "
        )


