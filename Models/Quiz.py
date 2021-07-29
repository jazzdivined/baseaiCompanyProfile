from setup import db

class QuizModel(db.Model):
    __tablename__ = 'questions'
    __bind_key__ = 'quiz'
    question_id = db.Column(db.Integer(), primary_key=True)
    question_path = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return (
            f"**question** "
            f"question_id: {self.question_id} "
            f"question_path: {self.question_path} "
        )