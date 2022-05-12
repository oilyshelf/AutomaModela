from BPMN.CombineStrategy import (ConcatStrategy, CrossStrategy,
                                  DiffrenceStrategy, EquiJoinStrategy,
                                  Intersecttrategy, JoinOnStrategy,
                                  LeftEquiJoinStrategy, LeftJoinOnStrategy,
                                  LeftNaturalJoinStrategy, NaturalJoinStrategy,
                                  OuterEquiJoinStrategy, OuterJoinOnStrategy,
                                  OuterNaturalJoinStrategy,
                                  RightEquiJoinStrategy, RightJoinOnStrategy,
                                  RightNaturalJoinStrategy, SubtractStrategy,
                                  ThetaStrategy, UnionStrategy)
from BPMN.DataTypes import DataTypes
from BPMN.FunctionBuilder import FunctionBuilder

combineFunctionDefinitions = [
    (
        NaturalJoinStrategy,
        {
            "text": "join",
        },
        {
            "text": "on index",
            "implicite": True
        },
    ),
    (
        LeftNaturalJoinStrategy,
        {
            "text": "left join",
        },
        {
            "text": "on index",
            "implicite": True
        },
    ),
    (
        RightNaturalJoinStrategy,
        {
            "text": "right join",
        },
        {
            "text": "on index",
            "implicite": True
        },
    ),
    (
        OuterNaturalJoinStrategy,
        {
            "text": "outer join",
        },
        {
            "text": "on index",
            "implicite": True
        },
    ),
    (
        JoinOnStrategy,
        {
            "text": "join on {column}",
            "types": {"column": (DataTypes.ATTR,)},
        },
    ),
    (
        LeftJoinOnStrategy,
        {
            "text": "left join on {column}",
            "types": {"column": (DataTypes.ATTR,)},
        },
    ),
    (
        RightJoinOnStrategy,
        {
            "text": "right join on {column}",
            "types": {"column": (DataTypes.ATTR,)},
        },
    ),
    (
        OuterJoinOnStrategy,
        {
            "text": "outer join on {column}",
            "types": {"column": (DataTypes.ATTR,)},
        },
    ),
    (
        EquiJoinStrategy,
        {
            "text": "join on {left_col} == {right_col}",
            "types":
                {
                    "left_col": (DataTypes.ATTR,),
                    "right_col": (DataTypes.ATTR,)
                },
        },
    ),
    (
        LeftEquiJoinStrategy,
        {
            "text": "left join on {left_col} == {right_col}",
            "types":
                {
                    "left_col": (DataTypes.ATTR,),
                    "right_col": (DataTypes.ATTR,)
                },
        },
    ),
    (
        RightEquiJoinStrategy,
        {
            "text": "right join on {left_col} == {right_col}",
            "types":
                {
                    "left_col": (DataTypes.ATTR,),
                    "right_col": (DataTypes.ATTR,)
                },
        },
    ),
    (
        OuterEquiJoinStrategy,
        {
            "text": "outer join on {left_col} == {right_col}",
            "types":
                {
                    "left_col": (DataTypes.ATTR,),
                    "right_col": (DataTypes.ATTR,)
                },
        },
    ),
    (
        ThetaStrategy,
        {
            "text": "join where {query}",
            "types":
                {
                    "query": (DataTypes.EXPR,),
                },
        },
    ),
    (
        ConcatStrategy,
        {
            "text": "concat",
        },
    ),
    (
        UnionStrategy,
        {
            "text": "union",
        },
    ),
    (
        Intersecttrategy,
        {
            "text": "intersect",
        },
    ),
    (
        DiffrenceStrategy,
        {
            "text": "difference",
        },
    ),
    (
        SubtractStrategy,
        {
            "text": "subtract",
        },
    ),
    (
        CrossStrategy,
        {
            "text": "cross",
        },
    ),


]

compiled_combine_funcs = [FunctionBuilder().build_function(*definition) for definition in combineFunctionDefinitions]
