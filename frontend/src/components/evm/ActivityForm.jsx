import { useState, useEffect } from 'react'
import Button from '../ui/Button'

const EMPTY_FORM = {
  name: '',
  bac: '',
  planned_progress: '',
  actual_progress: '',
  actual_cost: '',
}

const validate = (fields) => {
  const errors = {}
  if (!fields.name || fields.name.trim().length === 0) {
    errors.name = 'El nombre es requerido'
  }
  if (fields.bac === '' || Number(fields.bac) < 0) {
    errors.bac = 'El presupuesto debe ser mayor o igual a 0'
  }
  const pp = Number(fields.planned_progress)
  if (fields.planned_progress === '' || pp < 0 || pp > 100) {
    errors.planned_progress = 'El avance planificado debe estar entre 0 y 100'
  }
  const ap = Number(fields.actual_progress)
  if (fields.actual_progress === '' || ap < 0 || ap > 100) {
    errors.actual_progress = 'El avance real debe estar entre 0 y 100'
  }
  if (fields.actual_cost === '' || Number(fields.actual_cost) < 0) {
    errors.actual_cost = 'El costo real debe ser mayor o igual a 0'
  }
  return errors
}

const ActivityForm = ({ onSubmit, onCancel, initialValues = null, isLoading = false }) => {
  const [fields, setFields] = useState(EMPTY_FORM)
  const [errors, setErrors] = useState({})

  useEffect(() => {
    if (initialValues) {
      setFields({
        name: initialValues.name ?? '',
        bac: initialValues.bac ?? '',
        planned_progress: initialValues.planned_progress ?? '',
        actual_progress: initialValues.actual_progress ?? '',
        actual_cost: initialValues.actual_cost ?? '',
      })
    } else {
      setFields(EMPTY_FORM)
    }
  }, [initialValues])

  const handleChange = (e) => {
    const { name, value } = e.target
    setFields((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const validationErrors = validate(fields)
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors)
      return
    }
    setErrors({})
    onSubmit({
      name: fields.name.trim(),
      bac: String(fields.bac),
      planned_progress: String(fields.planned_progress),
      actual_progress: String(fields.actual_progress),
      actual_cost: String(fields.actual_cost),
    })
    if (!initialValues) {
      setFields(EMPTY_FORM)
    }
  }

  const isEditing = initialValues !== null

  return (
    <form onSubmit={handleSubmit} style={{ border: '1px solid #e5e7eb', padding: '1rem', borderRadius: '6px', marginBottom: '1rem' }}>
      <h3 style={{ marginTop: 0 }}>{isEditing ? 'Editar actividad' : 'Agregar actividad'}</h3>

      <div style={{ marginBottom: '0.75rem' }}>
        <label>Nombre de la actividad</label>
        <input
          name="name"
          value={fields.name}
          onChange={handleChange}
          style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
        />
        {errors.name && <span style={{ color: '#dc2626', fontSize: '0.8rem' }}>{errors.name}</span>}
      </div>

      <div style={{ marginBottom: '0.75rem' }}>
        <label>Presupuesto total (BAC)</label>
        <input
          name="bac"
          type="number"
          min="0"
          step="any"
          value={fields.bac}
          onChange={handleChange}
          style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
        />
        {errors.bac && <span style={{ color: '#dc2626', fontSize: '0.8rem' }}>{errors.bac}</span>}
      </div>

      <div style={{ marginBottom: '0.75rem' }}>
        <label>Avance planificado (%)</label>
        <input
          name="planned_progress"
          type="number"
          min="0"
          max="100"
          step="any"
          value={fields.planned_progress}
          onChange={handleChange}
          style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
        />
        {errors.planned_progress && (
          <span style={{ color: '#dc2626', fontSize: '0.8rem' }}>{errors.planned_progress}</span>
        )}
      </div>

      <div style={{ marginBottom: '0.75rem' }}>
        <label>Avance real (%)</label>
        <input
          name="actual_progress"
          type="number"
          min="0"
          max="100"
          step="any"
          value={fields.actual_progress}
          onChange={handleChange}
          style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
        />
        {errors.actual_progress && (
          <span style={{ color: '#dc2626', fontSize: '0.8rem' }}>{errors.actual_progress}</span>
        )}
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <label>Costo real (AC)</label>
        <input
          name="actual_cost"
          type="number"
          min="0"
          step="any"
          value={fields.actual_cost}
          onChange={handleChange}
          style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
        />
        {errors.actual_cost && (
          <span style={{ color: '#dc2626', fontSize: '0.8rem' }}>{errors.actual_cost}</span>
        )}
      </div>

      <div style={{ display: 'flex', gap: '0.5rem' }}>
        <Button type="submit" disabled={isLoading}>
          {isEditing ? 'Guardar cambios' : 'Agregar'}
        </Button>
        <Button variant="secondary" onClick={onCancel} disabled={isLoading}>
          Cancelar
        </Button>
      </div>
    </form>
  )
}

export default ActivityForm
