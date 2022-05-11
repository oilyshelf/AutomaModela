from BPMN.DataTypes import DataTypes
from BPMN.FunctionBuilder import FunctionBuilder
from BPMN.TransformationStrategy import (DoNothingStrategy, LoadExcelStrategy,
                                         RenameStrategy, ResetIndexStrategy,
                                         SaveExcelStrategy,
                                         SelectColumnStrategy,
                                         SelectRowsStrategy, SetIndexStrategy,
                                         addColumnStrategy, addRowStrategy,
                                         changeColumnStrategy,
                                         changeRowStrategy,
                                         deleteColumnStrategy,
                                         deleteDataStrategy, deleteRowStrategy,
                                         setColumnStrategy)

baseFunctionDefinitions = [
    (
        LoadExcelStrategy,
        {
            "text": "load data from excel file {file_name}",
            "types": {"file_name": (DataTypes.STRING,)}
        },
        {
            "text": "from the sheet {sheet_name}",
            "types": {"sheet_name": (DataTypes.STRING, DataTypes.INT)}
        },
        {
            "text": "and set the index to the column {index}", 
            "types": {"index": (DataTypes.ATTR, DataTypes.NONE)}
        },
    ),
    (
        SaveExcelStrategy,
        {
            "text": "save data to excel file {file_name}",
            "types": {"file_name": (DataTypes.STRING,)}
        },
        {
            "text": "in to the sheet {sheet_name}",
            "types": {"sheet_name": (DataTypes.STRING,)}
        },
        {
            "text": "and also keep the index", 
            "implicite": True
        },
    ),
    (
        SelectRowsStrategy,
        {
            "text": "select the rows where {query}",
            "types": {"query": (DataTypes.EXPR,)}
        },
    ),
    (
        SelectColumnStrategy,
        {
            "text": "select the columns named {column}",
            "types": {"column": (DataTypes.ATTR,)},
            "repeating": {"column": True},
        },
    ),
    (
        RenameStrategy,
        {
            "text": "rename column from {from_col} to {to_col}",
            "types": {"from_col": (DataTypes.ATTR,), "to_col": (DataTypes.ATTR,)},
        },
    ),
    (
        deleteDataStrategy,
        {
            "text": "delete the data",
        },
        {
            "text": "but keep the columns",
            "implicite": True
        },
    ),
    (
        addRowStrategy,
        {
            "text": "add row with the values {value}",
            "types": {"value": (DataTypes.FLOAT, DataTypes.INT, DataTypes.STRING, DataTypes.NONE, DataTypes.BOOL)},
            "repeating": {"value": True}
        },
    ),
    (
        addRowStrategy,
        {
            "text": "add row with the values {value}",
            "types": {"value": (DataTypes.ATTRMAP,)},
            "repeating": {"value": True}
        },
    ),
    (
        deleteRowStrategy,
        {
            "text": "delete row with the values {value}",
            "types": {"value": (DataTypes.FLOAT, DataTypes.INT, DataTypes.STRING, DataTypes.NONE, DataTypes.BOOL)},
            "repeating": {"value": True}
        },
    ),
    (
        deleteRowStrategy,
        {
            "text": "delete row with the values {value}",
            "types": {"value": (DataTypes.ATTRMAP,)},
            "repeating": {"value": True}
        },
    ),
    (
        changeRowStrategy,
        {
            "text": "change row from {org_value} to {new_value}",
            "types":
                {
                    "org_value": (DataTypes.FLOAT, DataTypes.INT, DataTypes.STRING, DataTypes.NONE, DataTypes.BOOL),
                    "new_value": (DataTypes.FLOAT, DataTypes.INT, DataTypes.STRING, DataTypes.NONE, DataTypes.BOOL),
                },
            "repeating":
                {
                    "org_value": True,
                    "new_value": True,
                }
        },
    ),
    (
        changeRowStrategy,
        {
            "text": "change row from {org_value} to {new_value}",
            "types":
                {
                    "org_value": (DataTypes.ATTRMAP,),
                    "new_value": (DataTypes.ATTRMAP,),
                },
            "repeating":
                {
                    "org_value": True,
                    "new_value": True,
                }
        },
    ),
    (
        addColumnStrategy,
        {
            "text": "add column {column} with the value {value}",
            "types":
                {
                    "column": (DataTypes.ATTR,),
                    "value": (DataTypes.EXPR,),
                },
        },
    ),
    (
        changeColumnStrategy,
        {
            "text": "change column {column} to the value {value}",
            "types":
                {
                    "column": (DataTypes.ATTR,),
                    "value": (DataTypes.EXPR,),
                },
        },
    ),
    (
        setColumnStrategy,
        {
            "text": "set column {column} to the value {value}",
            "types":
                {
                    "column": (DataTypes.ATTR,),
                    "value": (DataTypes.EXPR,),
                },
        },
    ),
    (
        deleteColumnStrategy,
        {
            "text": "delete column {column}",
            "types":
                {
                    "column": (DataTypes.ATTR,),
                },
        },
    ),
    (
        DoNothingStrategy,
        {
            "text": "do nothing",
        },
    ),
    (
        SetIndexStrategy,
        {
            "text": "set index to {column}",
            "types": {"column": (DataTypes.ATTR,)}
        },
    ),
    (
        ResetIndexStrategy,
        {
            "text": "reset the index",
        },
        {
            "text": "and keep the old one as a column",
            "implicite": True
        },
    ),
]

compiled_base_funcs = [FunctionBuilder().build_function(*definition) for definition in baseFunctionDefinitions]
