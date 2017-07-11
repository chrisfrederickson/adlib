from typing import Dict, List
from data_reader.dataset import EmailDataset
from data_reader.binary_input import Instance
from learners import learner
from sklearn.naive_bayes import BernoulliNB
from adversaries.cost_sensitive import CostSensitive

class AdversaryAware(object):
    def __init__(self, adversary = None ):
       self.adversary = adversary


    def set_params(self, params: Dict):
        """Set params for the initial learner.

        Defines default behavior, setting only BaseModel params

        Args:
            params (Dict): set of available params with updated values.

        """
        raise NotImplementedError

    def train(self):
        """Train on the set of training instances.

        """
        raise NotImplementedError

    def predict(self, instances):
        """Predict classification labels for the set of instances.

        Args:
            :param instances: matrix of instances shape (num_instances, num_feautres_per_instance)

        Returns:
            label classifications (List(int))

        """
        raise NotImplementedError

    def predict_proba(self, X):
        """
        outputs a list of log probability of prediction
        :param X: matrix of instances shape (num_instances, num_feautres_per_instance)
        :return: list of log probability
        """
        raise NotImplementedError

    def decision_function(self, X):
        raise NotImplementedError