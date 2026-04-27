"""
Marshmallow schemas for Activity validation and serialization.
"""

import marshmallow as ma
from marshmallow import validate


class ActivityCreateSchema(ma.Schema):
    """Validate the body of POST /projects/{id}/activities."""

    name = ma.fields.String(
        required=True,
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nombre de la actividad"},
    )
    bac = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0),
        metadata={"description": "Budget at Completion de la actividad"},
    )
    planned_progress = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0, max=100),
        metadata={"description": "Porcentaje de avance planificado (0-100)"},
    )
    actual_progress = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0, max=100),
        metadata={"description": "Porcentaje de avance real completado (0-100)"},
    )
    actual_cost = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0),
        metadata={"description": "Costo real incurrido hasta la fecha"},
    )


class ActivityUpdateSchema(ma.Schema):
    """Validate the body of PUT /activities/{id}."""

    name = ma.fields.String(validate=validate.Length(min=1, max=255))
    bac = ma.fields.Decimal(validate=validate.Range(min=0))
    planned_progress = ma.fields.Decimal(validate=validate.Range(min=0, max=100))
    actual_progress = ma.fields.Decimal(validate=validate.Range(min=0, max=100))
    actual_cost = ma.fields.Decimal(validate=validate.Range(min=0))


class EVMActivitySchema(ma.Schema):
    """Serialize EVM indicators for a single activity."""

    pv = ma.fields.String()
    ev = ma.fields.String()
    cv = ma.fields.String()
    sv = ma.fields.String()
    cpi = ma.fields.String(allow_none=True)
    spi = ma.fields.String(allow_none=True)
    eac = ma.fields.String(allow_none=True)
    vac = ma.fields.String(allow_none=True)
    cpi_interpretation = ma.fields.String()
    spi_interpretation = ma.fields.String()


class ActivityResponseSchema(ma.Schema):
    """Serialize the response body for activity endpoints."""

    id = ma.fields.String()
    project_id = ma.fields.String()
    name = ma.fields.String()
    bac = ma.fields.String()
    planned_progress = ma.fields.String()
    actual_progress = ma.fields.String()
    actual_cost = ma.fields.String()
    created_at = ma.fields.String(allow_none=True)
    updated_at = ma.fields.String(allow_none=True)
    evm = ma.fields.Nested(EVMActivitySchema)
