    """
    v2.4 Meta-Operators Module

    Universal integration layer and orchestration meta-operators.
    """

    from .meta_operators import (
        META_FLOW,
        META_RECURSION_GOVERNOR,
        META_TIME,
        META_ASCENT,
        META_COMPOSE,
        META_INTEGRATE,
        CompositionMode,
        Level,
        IntegrationStatus
    )

    __all__ = [
        'META_FLOW',
        'META_RECURSION_GOVERNOR',
        'META_TIME',
        'META_ASCENT',
        'META_COMPOSE',
        'META_INTEGRATE',
        'CompositionMode',
        'Level',
        'IntegrationStatus'
    ]

    __version__ = '2.4.0'
