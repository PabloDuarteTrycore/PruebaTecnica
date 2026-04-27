"""
Marshmallow schemas for Project validation and serialization.
"""

import marshmallow as ma
from marshmallow import validate


class ProjectCreateSchema(ma.Schema):
    """Validate the body of POST /projects/."""

    name = ma.fields.String(
        required=True,
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nombre del proyecto"},
    )
    description = ma.fields.String(
        load_default=None,
        allow_none=True,
        metadata={"description": "Descripcion opcional del proyecto"},
    )


class ProjectUpdateSchema(ma.Schema):
    """Validate the body of PUT /projects/{id}."""

    name = ma.fields.String(
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nuevo nombre del proyecto"},
    )
    description = ma.fields.String(
        allow_none=True,
        metadata={"description": "Nueva descripcion del proyecto"},
    )


class EVMProjectSchema(ma.Schema):
    """Serialize consolidated EVM indicators for a project."""

    total_bac = ma.fields.String()
    total_pv = ma.fields.String()
    total_ev = ma.fields.String()
    total_ac = ma.fields.String()
    cv = ma.fields.String()
    sv = ma.fields.String()
    cpi = ma.fields.String(allow_none=True)
    spi = ma.fields.String(allow_none=True)
    eac = ma.fields.String(allow_none=True)
    vac = ma.fields.String(allow_none=True)
    cpi_interpretation = ma.fields.String()
    spi_interpretation = ma.fields.String()


class ProjectResponseSchema(ma.Schema):
    """Serialize the response body for project endpoints."""

    id = ma.fields.String()
    name = ma.fields.String()
    description = ma.fields.String(allow_none=True)
    created_at = ma.fields.String(allow_none=True)
    updated_at = ma.fields.String(allow_none=True)
    activities = ma.fields.List(ma.fields.Dict(), dump_default=[])
    evm = ma.fields.Nested(EVMProjectSchema)
