# from Scikit-learn
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from regression_model.config.core import config
from feature_engine.selection import DropFeatures

dur_pipe = Pipeline([('drop_features', DropFeatures(features_to_drop=config.model_config.ref_var)),

                     ('scaler', MinMaxScaler()),
                     ('Lasso', Lasso(alpha=config.model_config.alpha,
                random_state=config.model_config.random_state))])