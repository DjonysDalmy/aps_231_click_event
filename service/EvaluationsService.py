import sqlite3

from repository.EvaluationsRepository import EvaluationRepository
from enumeration.Messages import Messages
from entity.Evaluations import Evaluations
class EvaluationService:

    def __init__(self):
        self.evaluation_repository = EvaluationRepository()
        self.evaluation_repository.set_up_evaluation_repository()

    def create_evaluation(self, user_id, event_id, rate, comment):
        evaluation = Evaluations(None, user_id, event_id, rate, comment)
        try:
            self.evaluation_repository.insert_evaluation(evaluation.get_id(), evaluation.get_user_id(), evaluation.get_event_id(), evaluation.get_rate(), evaluation.get_comment())
            return Messages.RATING_SUBMIT_OK.value
        except:
            return Messages.OPS.value