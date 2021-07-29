from setup import db

class MemberModel(db.Model):
    __tablename__ = 'members'
    __bind_key__ = 'teams'
    member_id = db.Column(db.Integer(), primary_key=True)
    member_name = db.Column(db.String(255), nullable=False)
    major = db.Column(db.String(255), nullable=False)
    motto = db.Column(db.String(255), nullable=True)
    img_path = db.Column(db.String(512), nullable=True)
    team_id = db.Column(db.Integer(), db.ForeignKey('teams.team_id'))


    def __repr__(self) -> str:
        return (
            f"**Member** "
            f"member_id: {self.member_id} "
            f"member_name: {self.member_name} "
            f"major: {self.major}"
            f"motto: {self.motto}"
            f"img_path: {self.img_path}"
            f"team_id: {self.team_id} "
        )
    
