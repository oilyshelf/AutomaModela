from BPMN.OpeningStrategy import CheckStartegy, CopyStrategy, EmptyStrategy, NewStrategy, ResetStartegy, SpliceStartegy  
from BPMN.FunctionBuilder import FunctionBuilder

poFunctionDefinitions = [
    (
        NewStrategy,
        {
            "text": "new",
        },
        {
            "text": "and keep",
            "implicite": True
        },
    ),
    (
        CopyStrategy,
        {
            "text": "copy",
        },
    ),
]
eoFunctionDefinitions = [
    (
        CheckStartegy,
        {
            "text": "check",
        },
        {
            "text": "but do not transform",
            "implicite": True
        },
    ),
    (
        EmptyStrategy,
        {
            "text": "is empty",
        },
    ),
]
ioFunctionDefinitions = [
    (
        SpliceStartegy,
        {
            "text": "splice",
        },
    ),
    (
        ResetStartegy,
        {
            "text": "reset",
        },
    ),
]

compiled_po_funcs = [FunctionBuilder().build_function(*definition) for definition in poFunctionDefinitions]
compiled_eo_funcs = [FunctionBuilder().build_function(*definition) for definition in eoFunctionDefinitions]
compiled_io_funcs = [FunctionBuilder().build_function(*definition) for definition in ioFunctionDefinitions]
