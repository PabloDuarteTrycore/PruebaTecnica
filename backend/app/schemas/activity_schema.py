"""
Marshmallow schemas for Activity validation and serialization.
"""

import marshmallow as ma
from marshmallow import ValidationError, validate, validates


class ActivityCreateSchema(ma.Schema):
    """Validate the body of POST /projects/{id}/activities."""

    name = ma.fields.String(
        required=True,
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nombre de la actividad"},
    )
    bac = ma.fields.Decimal(
        required=True,
        metadata={"description": "Budget at Completion de la actividad"},
    )
    planned_progress = ma.fields.Decimal(
        required=True,
        metadata={"description": "Porcentaje de avance planificado (0-100)"},
    )
    actual_progress = ma.fields.Decimal(
        required=True,
        metadata={"description": "Porcentaje de avance real completado (0-100)"},
    )
    actual_cost = ma.fields.Decimal(
        required=True,
        metadata={"description": "Costo real incurrido hasta la fecha"},
    )

    @validates("bac")
    def validate_bac(self, value):
        if value < 0:
            raise ValidationError("Must be greater than or equal to 0.")

    @validates("planned_progress")
    def validate_planned_progress(self, value):
        if value < 0 or value > 100:
            raise ValidationError(
                "Must be greater than or equal to 0 and less than or equal to 100."
            )

    @validates("actual_progress")
    def validate_actual_progress(self, value):
        if value < 0 or value > 100:
            raise ValidationError(
                "Must be greater than or equal to 0 and less than or equal to 100."
            )

    @validates("actual_cost")
    def validate_actual_cost(self, value):
        if value < 0:
            raise ValidationError("Must be greater than or equal to 0.")


class ActivityUpdateSchema(ma.Schema):
    """Validate the body of PUT /activities/{id}."""

    name = ma.fields.String(validate=validate.Length(min=1, max=255))
    bac = ma.fields.Decimal()
    planned_progress = ma.fields.Decimal()
    actual_progress = ma.fields.Decimal()
    actual_cost = ma.fields.Decimal()

    @validates("bac")
    def validate_bac(self, value):
        if value < 0:
            raise ValidationError("Must be greater than or equal to 0.")

    @validates("planned_progress")
    def validate_planned_progress(self, value):
        if value < 0 or value > 100:
            raise ValidationError(
                "Must be greater than or equal to 0 and less than or equal to 100."
            )

    @validates("actual_progress")
    def validate_actual_progress(self, value):
        if value < 0 or value > 100:
            raise ValidationError(
                "Must be greater than or equal to 0 and less than or equal to 100."
            )

    @validates("actual_cost")
    def validate_actual_cost(self, value):
        if value < 0:
            raise ValidationError("Must be greater than or equal to 0.")


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
