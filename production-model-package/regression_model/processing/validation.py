from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from regression_model.config.core import config

def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame
    '''Check model inputs for na values and filter'''
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)
    return validated_data

def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    '''check model inputs for unprocessable values'''
    #convert syntax error filed names (beginning with numbers)
    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None
    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors

class DurationInputSchema(BaseModel):
    Distance: Optional[int64]
    PLong: Optional[float64]
    PLatd: Optional[float64]
    DLong: Optional[float64]
    DLatd: Optional[float64]
    Haversine: Optional[float64]
    Pmonth: Optional[int64]
    Pday: Optional[int64]
    Phour: Optional[int64]
    Pmin: Optional[int64]
    PDweek: Optional[int64]
    Dmonth: Optional[int64]
    Dday: Optional[int64]
    Dhour: Optional[int64]
    Dmin: Optional[int64]
    DDweek: Optional[int64]
    Temp: Optional[float64]
    Precip: Optional[float64]
    Wind: Optional[float64]
    Humid: Optional[float64]
    Solar: Optional[float64]
    Snow: Optional[float64]
    GroundTemp: Optional[float64]
    Dust: Optional[float64]

class MultipleDataInputs(BaseModel):
    inputs: List[DurationInputSchema]